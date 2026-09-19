###############################################
# This file generates log files for various components of the agentic AI system. 
# It ensures structured logging, which is essential for debugging and monitoring system performance, 
# thereby enhancing the overall reliability and maintainability of the application.
###############################################
from pathlib import Path


# Defining a Path object for the directory where log files will be stored, named 'logs'.
LOG_DIR = Path("logs")

# Creating the log directory if it does not already exist; 'exist_ok=True' prevents errors if the directory exists.
LOG_DIR.mkdir(
    exist_ok=True
)


CHECKOUT_LOGS = """
2026-06-10 10:11:01 INFO Checkout started
2026-06-10 10:11:02 INFO Payment validated
2026-06-10 10:11:05 INFO Inventory reserved
2026-06-10 10:12:01 ERROR CheckoutService Transaction timeout
2026-06-10 10:12:03 ERROR Unable to acquire lock
2026-06-10 10:12:05 ERROR Checkout transaction failed
2026-06-10 10:12:07 WARN Customer abandoned cart
2026-06-10 10:12:10 ERROR Checkout transaction failed
2026-06-10 10:12:12 ERROR Checkout transaction failed
2026-06-10 10:12:15 WARN Checkout abandonment increasing
2026-06-10 10:12:18 ERROR Checkout transaction failed
2026-06-10 10:12:20 ERROR Checkout transaction failed
2026-06-10 10:12:25 WARN Checkout latency exceeded SLA
"""

DATABASE_LOGS = """
2026-06-10 10:12:01 ERROR DatabaseLockException
2026-06-10 10:12:02 ERROR Row lock held for 245 seconds
2026-06-10 10:12:04 ERROR Unable to acquire lock
2026-06-10 10:12:06 ERROR Deadlock detected
2026-06-10 10:12:08 ERROR Transaction rollback
2026-06-10 10:12:10 ERROR Lock contention threshold exceeded
2026-06-10 10:12:15 ERROR Checkout write failed
2026-06-10 10:12:18 ERROR Checkout write failed
2026-06-10 10:12:20 ERROR Deadlock detected
2026-06-10 10:12:23 ERROR Transaction rollback
2026-06-10 10:12:25 ERROR Checkout write failed
2026-06-10 10:12:27 ERROR Lock wait timeout exceeded
"""

APPLICATION_LOGS = """
2026-06-10 10:10:01 INFO Application startup
2026-06-10 10:11:01 INFO Checkout service online
2026-06-10 10:11:05 INFO Cart service healthy
2026-06-10 10:12:01 ERROR Service degradation detected
2026-06-10 10:12:05 ERROR Checkout endpoint latency spike
2026-06-10 10:12:10 ERROR Cart conversion drop detected
2026-06-10 10:12:15 WARN Revenue impact increasing
2026-06-10 10:12:20 ERROR Alert threshold exceeded
2026-06-10 10:12:25 ERROR Incident escalation triggered
2026-06-10 10:12:30 INFO PagerDuty notification sent
"""

INCIDENT_LOGS = """
2026-06-10 10:12:01 INCIDENT INC-1001 Checkout failures increasing
2026-06-10 10:12:05 INCIDENT INC-1001 Revenue impact observed
2026-06-10 10:12:10 INCIDENT INC-1001 Severity upgraded P1
2026-06-10 10:12:15 INCIDENT INC-1001 Engineering bridge opened
2026-06-10 10:12:20 INCIDENT INC-1001 Customer complaints rising
2026-06-10 10:12:25 INCIDENT INC-1001 Automated diagnosis initiated
2026-06-10 10:12:30 INCIDENT INC-1001 Awaiting RCA
"""





# Defining a function to generate log files with predefined content.
def generate_logs():

    # Creating a dictionary to hold the names and content of log files to be generated.
    logs = {

        # Mapping the log file name 'checkout.log' to its content stored in CHECKOUT_LOGS.
        "checkout.log": CHECKOUT_LOGS,

        # Mapping the log file name 'database.log' to its content stored in DATABASE_LOGS.
        "database.log": DATABASE_LOGS,

        # Mapping the log file name 'application.log' to its content stored in APPLICATION_LOGS.
        "application.log": APPLICATION_LOGS,

        # Mapping the log file name 'incident.log' to its content stored in INCIDENT_LOGS.
        "incident.log": INCIDENT_LOGS
    # Closing the dictionary definition.
    }

    # Iterating through the dictionary to create each log file with its associated content.
    for file_name, content in logs.items():

        # Opening each log file in write mode within the specified directory.
        with open(
            LOG_DIR / file_name,
            "w"
        ) as file:

            # Writing the content to the log file.
            file.write(content)


if __name__ == "__main__":

    generate_logs()