##################################################################################
# The  workflow_runner.py file defines a WorkflowRunner class with an asynchronous method 
# run_incident. This method locks the database to ensure safe access and initializes a state 
# with a unique incident ID. This structure is likely part of a larger workflow management 
# system, where incidents are processed asynchronously.
# ##################################################################################

import uuid
from datetime import datetime

from app.graph.workflow import (
    workflow
)

from app.graph.state import (
    AgenticWorkflowState
)

# This line imports the db object from the simulated_database module located in the app.db 
# package. This likely provides access to a database or a simulated database for testing purpose

from app.db.simulated_database import (
    db
)

from app.runtime.runtime_store import (
    runtime_store
)



#A class named  WorkflowRunner is defined. This class will contain methods related to running workflows.
class WorkflowRunner:

    #The run_incident method is defined as an asynchronous function. This means it can perform non-blocking operations.
    async def run_incident(self):

        # The first line inside this method calls lock_db() on the db object. This likely locks the
        # database to prevent concurrent access, ensuring data integrity during the execution of this method.
        db.lock_db()

        #Here, a state variable is being initialized with an instance of AgenticWorkflowState.
        state = (
            AgenticWorkflowState(
                incident_id=str(
                    uuid.uuid4() #An incident_id is generated using uuid.uuid4(), which creates a unique identifier for the incident. The str() function converts this UUID to a string format.
                )
            )
        )

        # Add these lines here
        state.checkout_failure_before = 35
        state.checkout_failure_after = 35
        state.database_lock_count = 17

        start_time = datetime.utcnow()

        result_dict = await workflow.ainvoke(state)

        end_time = datetime.utcnow()

        duration = (
            end_time - start_time
        ).total_seconds()

        result_dict["mttr_seconds"] = duration

        result = AgenticWorkflowState(
            **result_dict
        )

        #result = (
        #    await workflow.ainvoke(
        #        state
        #    )
        #)

        print("RESULT TYPE =", type(result))
        print("RESULT =", result)
   
        if isinstance(result, dict):
            result["mttr_seconds"] = duration
            final_state = result
        else:
            state.mttr_seconds = duration
            final_state = state

        #result["mttr_seconds"] = (
        #    end_time - start_time
        #).total_seconds()

        runtime_store.add_message(
            f"Workflow completed in {end_time - start_time} seconds"
        )

        runtime_store.set_workflow_state(
            result
        )

        runtime_store.set_execution(
            {
                "completed": True
            }
        )


        return result

runner = WorkflowRunner()