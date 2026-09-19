################################################################
# ActionAgentThis agent is responsible for handling actions related to the # checkout process.
# The action_agent.py file defines the ActionAgent class, which is responsible for executing 
# specific actions based on the state of the system. It enhances the agentic AI system's 
# responsiveness by automating actions like unlocking the database or restarting the 
# connection pool. This automation improves efficiency and ensures timely interventions, 
# ultimately contributing to system stability and reliability.
#################################################################
from datetime import datetime

from app.db.simulated_database import db

from app.utils.logger import get_logger


logger = get_logger(
    "ActionAgent"
)


class ActionAgent:

    async def execute(
            self,
            state
    ):

        logger.info(
            "Action Agent Started"
        )

        if (
            state.selected_action
            == "unlock_database"
        ):

            db.unlock_db()
            state.database_lock_count = 0
            state.checkout_failure_after = 1.0

            logger.info(
                "Database unlocked successfully"
            )

            state.action_status = (
                "completed"
            )

        elif (
            state.selected_action
            == "restart_connection_pool"
        ):

            logger.info(
                "Connection pool restarted"
            )

            state.action_status = (
                "completed"
            )

        else:

            logger.warning(
                "Manual intervention required"
            )

            state.action_status = (
                "manual_intervention"
            )

        return state