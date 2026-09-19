# Importing the Path class from the pathlib module to handle filesystem paths in a flexible way.
from pathlib import Path

# Importing the get_logger function from the logger module to set up logging for this agent.
from app.utils.logger import get_logger


# Creating a logger instance for the DiscoveryAgent to log its activities and findings.
logger = get_logger(
    "DiscoveryAgent"
)


# Defining the DiscoveryAgent class, responsible for identifying issues based on log files.
class DiscoveryAgent:

    # Defining a list of keywords that indicate potential errors in the logs.
    ERROR_KEYWORDS = [

        "ERROR",
        "LOCK",
        "DEADLOCK",
        "FAILED",
        "TIMEOUT",
        "ABANDONMENT"
    ]

    # Defining an asynchronous method to execute the discovery process on the provided state.
    async def execute(
            self,
            state
    ):

        logger.info(
            "Discovery Agent Started"
        )

        # Setting the log directory path where log files are stored.
        log_dir = Path("logs")

        # Initializing a list to hold the discovered log files that contain error keywords.
        discovered = []

        # Iterating through all log files in the specified log directory.
        for file in log_dir.glob("*.log"):

            # Reading the content of the current log file as text.
            content = file.read_text()

            # Checking if any of the defined error keywords are present in the log file content.

            for keyword in self.ERROR_KEYWORDS:

                # Checking if any of the defined error keywords are present in the log file content.
                if keyword.lower() in content.lower():

                    # Appending the name of the file to the discovered list if an error keyword is found.
                    discovered.append(
                        str(file)
                    )

                    break

        # Updating the state with the list of discovered logs that contain errors.
        state.discovered_logs = discovered

        # Updating the state to indicate if any issues were discovered based on the log files.
        state.suspected_issue = (
            len(discovered) > 0
        )

        logger.info(
            f"Discovered Logs: {len(discovered)}"
        )

        return state