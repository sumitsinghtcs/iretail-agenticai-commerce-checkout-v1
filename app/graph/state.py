##################################
#  State.py
# The file is structured to manage and track the execution of agents within a workflow, 
# providing a clear schema for recording relevant details about each execution and the 
# overall state of the workflow. This is likely part of a larger system focused on incident 
# management or automated healing processes.
# The state.py file defines two main classes using Pydantic, which is a data validation and 
# settings management library in Python. H
##################################


from typing import List # 

from pydantic import BaseModel

# This class represents a record of an agent's execution.
class AgentExecutionRecord(BaseModel):

    agent_name: str #agent_name: The name of the agent. 

    status: str #status: The current status of the agent (e.g., running, completed).

    start_time: str #start_time: The time when the agent started executing.

    end_time: str #end_time: The time when the agent finished executing.

    duration_ms: float #duration_ms: The duration of the execution in milliseconds.


class AgenticWorkflowState(BaseModel):

    incident_id: str # incident_id: An identifier for the incident being addressed.

    suspected_issue: bool = False #suspected_issue: A boolean indicating if there is a suspected issue.
    
    validation_passed: bool = False #validation_passed: A boolean indicating if validation checks have passed.

    root_cause: str = "" #root_cause: A string describing the root cause of the issue.

    confidence: float = 0.0 #confidence: A float representing the confidence level in the diagnosis.

    selected_action: str = "" #selected_action: The action chosen to address the issue.

    action_status: str = "" #action_status: The status of the selected action.

    healing_successful: bool = False #healing_successful: A boolean indicating if the healing action was successful.

    report_path: str = "" #report_path: A string indicating the path to the report generated.

    discovered_logs: List[str] = [] #discovered_logs: A list of logs that were discovered during the process.

    evidence: List[str] = [] #evidence: A list of evidence files associated with the incident.

    agent_trace: List[AgentExecutionRecord] = [] #agent_trace: A list of agent execution records.

    # Dynamic Metrics
    checkout_failure_before: float = 35.0
    checkout_failure_after: float = 35.0
    database_lock_count: int = 17
    mttr_seconds: float = 0.0