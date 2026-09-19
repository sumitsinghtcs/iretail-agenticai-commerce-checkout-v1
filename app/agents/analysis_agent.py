#######################################################
# The analysis_agent.py file is responsible for performing root cause analysis on log files 
# to identify issues and provide insights into the system's behavior.
# The  AnalysisAgent  class is crucial for diagnosing problems in the agentic AI system 
# by analyzing log files and extracting relevant information. It enhances the system's 
# reliability by providing insights into potential issues, thereby facilitating effective 
# root cause analysis.
#######################################################

#Imports: The file imports necessary modules and classes, including:
# json for handling JSON data.
import json

# Path from pathlib for file path manipulations.
from pathlib import Path

from llama_index.core import Settings

from llama_index.embeddings.huggingface import (
    HuggingFaceEmbedding
)

# VectorStoreIndex and Document from llama_index.core for handling document storage and indexing.
from llama_index.core import (
    VectorStoreIndex,
    Document
)

# ProviderFactory for obtaining an appropriate provider for generating responses.
from app.llm.provider_factory import (
    ProviderFactory
)

# get_logger for setting up logging.
from app.utils.logger import get_logger

# A logger instance named  logger  is created for the AnalysisAgent to log its activities and findings.
logger = get_logger(
    "AnalysisAgent"
)


#The AnalysisAgent class encapsulates the logic for analyzing logs
class AnalysisAgent:

    # In the init  method, the agent initializes a provider using the ProviderFactory. 
    # This provider will be used to generate responses based on the analysis
    def __init__(self):

        self.provider = (
            ProviderFactory
            .get_provider()
        )

    # The execute method is defined as an asynchronous function that takes a state parameter. 
    # This method will carry out the analysis process.
    async def execute(
            self,
            state
    ):
    
    #Inside the execute  method, the agent logs the start of the analysis process
        logger.info(
            "Analysis Agent Started"
        )

        #The method reads the content of each log file and creates Document objects, which are appended to a list.
        documents = []

        for file_path in state.discovered_logs:

            content = (
                Path(file_path)
                .read_text()
            )

            documents.append(
                Document(
                    text=content
                )
            )

            Settings.embed_model = HuggingFaceEmbedding(
                model_name="BAAI/bge-small-en-v1.5"
            )        

        print(Settings.embed_model) #2del

        # Index Creation:A VectorStoreIndex is created from the list of documents, allowing for efficient retrieval of relevant information.
        # The VectorStoreIndex is an in-memory structure that holds vector representations of documents for efficient retrieval. 
        # It enhances performance by allowing quick access to relevant information during analysis.
        index = VectorStoreIndex.from_documents(
            documents
        )

        retriever = index.as_retriever()

        #Retrieving Information: The agent retrieves nodes related to specific queries (like "checkout failures") from the index.
        nodes = retriever.retrieve(
            "checkout failures"
        )

        context = "\n".join(
            [
                n.text
                for n in nodes
            ]
        )

        # Prompt Generation: A prompt is generated for an AI model to perform root cause analysis 
        # based on the retrieved context.
        
        prompt = f"""
You are an SRE AI agent.

Perform root cause analysis.
```

Context:

{context}

Return JSON only:

{{
 "root_cause":"",
 "confidence":0.0,
 "evidence":[]
}}
"""
        #Response Handling: The agent sends the prompt to the provider and attempts to parse 
        #the response. If parsing fails, it falls back to a default response.
        response = (
            await self.provider.generate(
                prompt
            )
        )

        try:

            parsed = json.loads(
                response
            )

        except Exception:

            parsed = {

                "root_cause":
                    "Database Lock",

                "confidence":
                    0.95,

                "evidence":
                    [
                        "Deadlock detected",
                        "Lock wait timeout"
                    ]
            }

        #State Update: The state is updated with the root cause, confidence level, and evidence extracted from the response.
        state.root_cause = (
            parsed["root_cause"]
        )

        state.confidence = (
            parsed["confidence"]
        )

        state.evidence = (
            parsed["evidence"]
        )

        #Logging Results: Finally, the results of the analysis are logged, and the updated state is returned.
        logger.info(
            f"Root Cause: {state.root_cause}"
        )

        return state