########################################################################
# Summary: This file provides data models for root cause analysis, decision making, 
# and validation responses, ensuring structured data handling in the application.
########################################################################

# Importing BaseModel from Pydantic, a data validation and settings management library in Python.
from pydantic import BaseModel


# RCAResponse class inherits from BaseModel and is used to define the structure of a root cause analysis response.
class RCAResponse(BaseModel):

    # root_cause: A string that holds the root cause identified during analysis.
    root_cause: str
    # confidence: A float that represents the confidence level in the identified root cause.
    confidence: float
    # evidence: A list of strings that contains evidence supporting the root cause analysis.
    evidence: list[str]


# DecisionResponse class inherits from BaseModel and defines the structure of a decision response.
class DecisionResponse(BaseModel):

    # selected_action: A string that specifies the action chosen to address the incident.
        selected_action: str




# ValidationResponse class inherits from BaseModel and is used to define the structure of a validation response.
class ValidationResponse(BaseModel):

    validation_passed: bool