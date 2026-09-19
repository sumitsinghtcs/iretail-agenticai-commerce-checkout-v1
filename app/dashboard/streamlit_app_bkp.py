import json
import requests

import streamlit as st
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import networkx as nx

st.set_page_config(
    page_title="Agentic AI Self Healing",
    layout="wide"
)

PRIMARY = "#EC6608"
SECONDARY = "#2F2F2F"
SUCCESS = "#2E7D32"
WARNING = "#F9A825"
ERROR = "#C62828"

API_URL = "http://localhost:8000"

st.title(
    "🧠 Agentic AI Self-Healing Dashboard"
)

col1, col2 = st.columns(
    [1, 5]
)

with col1:

    if st.button(
        "Run Incident"
    ):

        requests.post(
            f"{API_URL}/run-incident"
        )

        st.success(
            "Incident Executed"
        )

###############################################
#Load Incident Data

try:

    status = requests.get(
        f"{API_URL}/incident-status"
    ).json()

except Exception:

    status = {}

################################################
#Executive KPI Cards

st.subheader(
    "Executive KPIs"
)

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.metric(
        "Incident Count",
        "1"
    )

with k2:
    st.metric(
        "Checkout Failure %",
        "35%"
    )

with k3:
    st.metric(
        "Database Locks",
        "17"
    )

with k4:
    st.metric(
        "MTTR",
        "2.3 min"
    )

with k5:
    st.metric(
        "Healing Success",
        "100%"
    )


####################################################
#Recovery Visualisation

st.subheader(
    "Recovery Trend"
)

recovery_df = pd.DataFrame(
    {
        "Stage":
            [
                "Before",
                "After"
            ],

        "Checkout Failure":
            [
                35,
                1
            ]
    }
)

fig = px.line(
    recovery_df,
    x="Stage",
    y="Checkout Failure",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

#################################################
#RCA PIE CHART

st.subheader(
    "Root Cause Distribution"
)

rca_df = pd.DataFrame(
    {
        "Cause":
            [
                "Database Lock",
                "Network",
                "Application",
                "Unknown"
            ],

        "Count":
            [
                82,
                8,
                6,
                4
            ]
    }
)

fig = px.pie(
    rca_df,
    names="Cause",
    values="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

#Agent Flow Visualisation
st.subheader(
    "Agent Workflow"
)

G = nx.DiGraph()

agents = [

    "Discovery",

    "PreValidation",

    "Analysis",

    "Decision",

    "Action",

    "PostValidation",

    "Reporting"
]

for i in range(
        len(agents) - 1
):

    G.add_edge(
        agents[i],
        agents[i + 1]
    )

pos = nx.spring_layout(
    G,
    seed=42
)

edge_x = []
edge_y = []

for edge in G.edges():

    x0, y0 = pos[
        edge[0]
    ]

    x1, y1 = pos[
        edge[1]
    ]

    edge_x.extend(
        [x0, x1, None]
    )

    edge_y.extend(
        [y0, y1, None]
    )

edge_trace = go.Scatter(
    x=edge_x,
    y=edge_y,
    mode="lines"
)

node_x = []
node_y = []

for node in G.nodes():

    x, y = pos[node]

    node_x.append(x)

    node_y.append(y)

node_trace = go.Scatter(
    x=node_x,
    y=node_y,
    mode="markers+text",
    text=list(
        G.nodes()
    ),
    textposition="top center",
    marker=dict(
        size=35
    )
)

fig = go.Figure(
    data=[
        edge_trace,
        node_trace
    ]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

########################################
# Agent Timeline

st.subheader(
    "Agent Timeline"
)

timeline_df = pd.DataFrame(
    {
        "Agent":
            agents,

        "Start":
            [
                0,
                1,
                2,
                3,
                4,
                5,
                6
            ],

        "Finish":
            [
                1,
                2,
                3,
                4,
                5,
                6,
                7
            ]
    }
)

fig = px.timeline(
    timeline_df,
    x_start="Start",
    x_end="Finish",
    y="Agent"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

######################################################
# Incident Summary

st.subheader(
    "Incident Summary"
)

if status:

    st.json(
        status
    )

#######################################################
#Live Agent Messages

st.subheader(
    "Agent Messages"
)

messages = [

    "Discovery Agent Started",

    "Discovery Agent Completed",

    "PreValidation Started",

    "Analysis Started",

    "Database Lock Identified",

    "Unlock Database",

    "Post Validation Successful",

    "Reporting Complete"
]

for message in messages:

    st.write(
        f"✅ {message}"
    )

########################################
# Metrics Panel

st.subheader(
    "Telemetry Metrics"
)

try:

    metrics = requests.get(
        f"{API_URL}/metrics"
    ).json()

    st.json(
        metrics
    )

except Exception:

    st.warning(
        "Metrics unavailable"
    )

