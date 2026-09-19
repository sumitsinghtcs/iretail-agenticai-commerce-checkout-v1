from datetime import datetime


class RuntimeStore:

    def __init__(self):

        self.last_execution = None

        self.agent_messages = []

        self.workflow_state = None

    def add_message(
            self,
            message
    ):

        self.agent_messages.append(
            {
                "timestamp":
                    datetime.utcnow().isoformat(),

                "message":
                    message
            }
        )

    def set_workflow_state(
            self,
            state
    ):

        self.workflow_state = state

    def set_execution(
            self,
            execution
    ):

        self.last_execution = execution


runtime_store = RuntimeStore()