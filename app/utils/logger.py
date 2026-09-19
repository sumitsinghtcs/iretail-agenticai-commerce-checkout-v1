#####################################
# The logger.py  file sets up a logging system for the 
# application, allowing for both file and console logging. 
# This is useful for tracking application behavior, debugging,
# and monitoring. The centralized logging configuration helps
#  maintain consistency across different parts of the application.
#####################################


#logging: This module is part of the standard library and provides a flexible framework for emitting log messages from Python programs.
#Path: Imported from the pathlib module to handle file system paths in a more versatile way.
#LOG_FILE: A constant variable that represents the path to the log file.

import logging

from pathlib import Path


# LOG_DIR: This sets the directory where log files will be stored, named  logs
# .mkdir(exist_ok=True): This creates the  logs directory if it doesn't already exist, preventing an error if it does

LOG_DIR = Path("logs")

LOG_DIR.mkdir(
    exist_ok=True
)


# This line specifies the path for the log file, which will be named agentic_ai.log and located in the logs directory.
LOG_FILE = LOG_DIR / "agentic_ai.log"

# This function is defined to create and configure a logger object.
def get_logger(
        name: str
):

    #getLogger(name): Retrieves a logger with the specified name. If it doesn't exist, it creates one.
    logger = logging.getLogger(name)
    
    #setLevel(logging.INFO): Sets the logging level to INFO, meaning it will capture all messages at this level and above (e.g., WARNING, ERROR).
    logger.setLevel(logging.INFO)

    #This checks if the logger already has handlers (i.e., destinations for log messages). If it does, it returns the existing logger to avoid adding multiple handlers.
    if logger.handlers:
        return logger

    #This line creates a formatter that specifies the format of the log messages, including the timestamp, log level, logger name, and the actual message.
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    #File Handler: Sends log messages to the specified log file.
    file_handler = logging.FileHandler(LOG_FILE)

    file_handler.setFormatter(formatter)

    #Console Handler: Sends log messages to the console (standard output).
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    #This adds both the file and console handlers to the logger, allowing it to log messages to both destinations.
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    #Finally, the configured logger is returned, ready to be used throughout the application.
    return logger