#############################################
# The decision_agent.py file is responsible for making decisions based on the provided state.
# It sets up logging for the agent and defines an asynchronous method to execute the decision-making process.

#The  DecisionAgent class is crucial for determining the appropriate actions based on the identified root causes.
# By automating the decision-making process, it enhances the efficiency and effectiveness of the agentic AI system, 
# allowing for quicker responses to issues.
#############################################

#The file imports the get_logger function from the logger module to set up logging for the agent.
from app.utils.logger import get_logger

#A logger instance named logger is created for the DecisionAgent to log its activities and findings.
logger = get_logger(
    "DecisionAgent"
)

#The  DecisionAgent class encapsulates the logic for making decisions based on the root cause.
class DecisionAgent:

    #The execute method is defined as an asynchronous function that takes a state parameter. This method will carry out the decision-making process.
    async def execute(
            self,
            state
    ):

        logger.info(
            "Decision Agent Started"
        )

        #The method retrieves the root_cause from the provided state and converts it to lowercase for consistent comparison.
        root_cause = (
            state.root_cause
            .lower()
        )

        if "database" in root_cause:

            action = (
                "unlock_database"
            )

        elif "connection" in root_cause:

            action = (
                "restart_connection_pool"
            )

        else:

            action = (
                "manual_intervention"
            )

        #The chosen action is stored in the state object.
        state.selected_action = (
            action
        )

        logger.info(
            f"Action={action}"
        )

        return state