#Path: This is imported from the pathlib module to handle file paths in a more flexible way.
#load_dotenv: This function is imported from the dotenv module to load environment variables from a .env file.
#os: This module provides a way to use operating system-dependent functionality, including environment variables.

from pathlib import Path

from dotenv import load_dotenv

import os


BASE_DIR = Path(__file__).resolve().parents[2]
#This line sets BASE_DIR to the path of the project's root directory by resolving the current file's path (__file__) and navigating two levels up in the directory structure.

load_dotenv(BASE_DIR / ".env")
#This line loads environment variables from a .env file located in the base directory. These variables can be accessed later in the code.

#A class named  Settings is defined to encapsulate application configuration settings.
class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "Agentic AI Self Healing"
    )

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "dev"
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    DATABASE_FILE = os.getenv(
        "DATABASE_FILE",
        "checkout.db"
    )

    LLM_PROVIDER = os.getenv(
        "LLM_PROVIDER",
        "groq"
    )

    DEFAULT_MODEL = os.getenv(
        "DEFAULT_MODEL",
        "llama-3.3-70b-versatile"
    )

    GROQ_API_KEY = os.getenv(
        "GROQ_API_KEY"
    )

    GEMINI_API_KEY = os.getenv(
        "GEMINI_API_KEY"
    )

    OPENROUTER_API_KEY = os.getenv(
        "OPENROUTER_API_KEY"
    )

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )


settings = Settings()