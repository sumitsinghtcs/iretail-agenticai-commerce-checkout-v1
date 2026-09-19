from pathlib import Path

import json

from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.services.workflow_runner import (
    runner
)

from app.runtime.runtime_store import (
    runtime_store
)


app = FastAPI(
    title="Agentic AI Self Healing"
)


@app.get("/")
async def health():

    return {
        "status": "healthy"
    }


@app.post("/run-incident")
async def run_incident():

    result = (
        await runner.run_incident()
    )

    return {
        "incident_id": result.incident_id,
        "root_cause": result.root_cause,
        "healing_successful": result.healing_successful,
        "checkout_failure_before": result.checkout_failure_before,
        "checkout_failure_after": result.checkout_failure_after,
        "database_lock_count": result.database_lock_count,
        "mttr_seconds": result.mttr_seconds
    }


@app.get("/incident-status")
async def incident_status():

    state = (
        runtime_store.workflow_state
    )

    if not state:

        return {
            "status":
                "No Incident Executed"
        }

    print(type(state))
    print(state.model_dump())
    
    return state.model_dump()


@app.get("/agent-trace")
async def agent_trace():

    state = (
        runtime_store.workflow_state
    )

    if not state:

        return []

    return state.agent_trace


@app.get("/metrics")
async def metrics():

    metrics_file = (
        Path("metrics")
        /
        "metrics.json"
    )

    if not metrics_file.exists():

        return []

    with open(metrics_file) as f:

        return json.load(f)


@app.get("/report")
async def report():

    report_file = (
        Path("reports")
        /
        "incident_report.html"
    )

    return FileResponse(
        report_file
    )