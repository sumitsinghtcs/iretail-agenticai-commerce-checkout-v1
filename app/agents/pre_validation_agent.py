###################################################################
# PreValidationAgent: This class is responsible for executing the pre-validation process on the provided state.
# It sets up logging for the agent and defines an asynchronous method to execute the pre-validation process.

# Purpose and Benefit:
# The  PreValidationAgent  class is crucial for ensuring that the system is in a valid state
# before proceeding with further actions. By checking logs for specific error messages, 
# it helps identify potential issues early, thereby enhancing the reliability and robustness 
# of the overall agentic AI system.
###################################################################

# Importing the get_logger function from the logger module to set up logging for this agent.
from app.utils.logger import get_logger


# Creating a logger instance for the PreValidationAgent to log its activities and findings.
logger = get_logger(
    "PreValidationAgent"
)


class PreValidationAgent:

    # Defining an asynchronous method to execute the pre-validation process on the provided state.
    async def execute(
            self,
            state
    ):

        # Logging the start of the pre-validation process.
        logger.info(
            "Pre Validation Started"
        )

        # Initializing a counter for the number of pieces of evidence found during validation.
        evidence_count = 0

        #File Processing: The method iterates through the discovered logs in the provided 
        # state, reading each log file's content.

        for file_path in state.discovered_logs:

            with open(file_path) as file:

                content = file.read()

                # Keyword Checks:The method checks for specific keywords (like "lock", 
                # "deadlock", or "transaction failed") in the log content to determine 
                # if any issues are present.

                if "lock" in content.lower():
                    evidence_count += 1

                if "deadlock" in content.lower():
                    evidence_count += 1

                if "transaction failed" in content.lower():
                    evidence_count += 1

        #State Update:The state is updated based on the evidence count, indicating whether the validation passed or failed.
        state.validation_passed = (
            evidence_count >= 3
        )

        #Logging Results: Finally, the results of the validation are logged, and the updated state is returned
        logger.info(
            f"Validation Passed: {state.validation_passed}"
        )

        # Returning the updated state after validation is complete.
        return state

