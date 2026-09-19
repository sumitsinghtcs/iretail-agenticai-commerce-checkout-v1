#This is main langgraph orchestrator

import uuid

from datetime import datetime

from langgraph.graph import (
    StateGraph,
    END
)

from app.graph.state import (
    AgenticWorkflowState
)

from app.agents.discovery_agent import (
    DiscoveryAgent
)

from app.agents.pre_validation_agent import (
    PreValidationAgent
)

from app.agents.analysis_agent import (
    AnalysisAgent
)

from app.agents.decision_agent import (
    DecisionAgent
)

from app.agents.action_agent import (
    ActionAgent
)

from app.agents.post_validation_agent import (
    PostValidationAgent
)

from app.agents.reporting_agent import (
    ReportingAgent
)

from app.utils.telemetry import (
    telemetry
)

from app.utils.logger import (
    get_logger
)


logger = get_logger(
    "Workflow"
)


discovery_agent = DiscoveryAgent()

pre_validation_agent = (
    PreValidationAgent()
)

analysis_agent = (
    AnalysisAgent()
)

decision_agent = (
    DecisionAgent()
)

action_agent = (
    ActionAgent()
)

post_validation_agent = (
    PostValidationAgent()
)

reporting_agent = (
    ReportingAgent()
)

async def discovery_node(
        state
):

    start = (
        telemetry.start_timer()
    )

    result = (
        await discovery_agent.execute(
            state
        )
    )

    telemetry.stop_timer(
        "discovery_agent",
        start
    )

    return result


async def validation_node(
        state
):

    start = (
        telemetry.start_timer()
    )

    result = (
        await pre_validation_agent.execute(
            state
        )
    )

    telemetry.stop_timer(
        "pre_validation_agent",
        start
    )

    return result


async def analysis_node(
        state
):

    start = (
        telemetry.start_timer()
    )

    result = (
        await analysis_agent.execute(
            state
        )
    )

    telemetry.stop_timer(
        "analysis_agent",
        start
    )

    return result


async def decision_node(
        state
):

    start = (
        telemetry.start_timer()
    )

    result = (
        await decision_agent.execute(
            state
        )
    )

    telemetry.stop_timer(
        "decision_agent",
        start
    )

    return result


async def action_node(
        state
):

    start = (
        telemetry.start_timer()
    )

    result = (
        await action_agent.execute(
            state
        )
    )

    telemetry.stop_timer(
        "action_agent",
        start
    )

    return result


async def post_validation_node(
        state
):

    start = (
        telemetry.start_timer()
    )

    result = (
        await post_validation_agent.execute(
            state
        )
    )

    telemetry.stop_timer(
        "post_validation_agent",
        start
    )

    return result


async def reporting_node(
        state
):

    start = (
        telemetry.start_timer()
    )

    result = (
        await reporting_agent.execute(
            state
        )
    )

    telemetry.stop_timer(
        "reporting_agent",
        start
    )

    return result

graph = StateGraph(
    AgenticWorkflowState
)

graph.add_node(
    "Discovery",
    discovery_node
)

graph.add_node(
    "PreValidation",
    validation_node
)

graph.add_node(
    "Analysis",
    analysis_node
)

graph.add_node(
    "Decision",
    decision_node
)

graph.add_node(
    "Action",
    action_node
)

graph.add_node(
    "PostValidation",
    post_validation_node
)

graph.add_node(
    "Reporting",
    reporting_node
)

graph.set_entry_point(
    "Discovery"
)

graph.add_edge(
    "Discovery",
    "PreValidation"
)

graph.add_edge(
    "PreValidation",
    "Analysis"
)

graph.add_edge(
    "Analysis",
    "Decision"
)

graph.add_edge(
    "Decision",
    "Action"
)

graph.add_edge(
    "Action",
    "PostValidation"
)

graph.add_edge(
    "PostValidation",
    "Reporting"
)

graph.add_edge(
    "Reporting",
    END
)

workflow = graph.compile()