############################################
# ReportingAgentThis agent is responsible for generating reports based on the state of the system.
# The reporting_agent.py file defines the ReportingAgent class, which is responsible for generating reports based on the state of the system.
# It enhances the agentic AI system's responsiveness by providing a structured way to share findings and insights.
############################################
# The  reporting_agent.py  file defines the ReportingAgent class, which is responsible for generating various types of reports 
# (HTML, PDF, and JSON) based on the system's state. By automating the reporting process, it enhances transparency and facilitates 
# better decision-making within the agentic AI system. This contributes to improved monitoring and analysis of incidents, 
# ultimately leading to more effective system management.
#

from pathlib import Path

import json

from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from app.utils.logger import get_logger


logger = get_logger(
    "ReportingAgent"
)


REPORT_DIR = Path(
    "reports"
)

REPORT_DIR.mkdir(
    exist_ok=True
)


class ReportingAgent:

    async def execute(
            self,
            state
    ):

        logger.info(
            "Reporting Agent Started"
        )

        html_path = (
            REPORT_DIR /
            "incident_report.html"
        )

        pdf_path = (
            REPORT_DIR /
            "incident_report.pdf"
        )

        json_path = (
            REPORT_DIR /
            "incident_summary.json"
        )

        self.generate_html(
            state,
            html_path
        )

        self.generate_pdf(
            state,
            pdf_path
        )

        self.generate_json(
            state,
            json_path
        )

        state.report_path = (
            str(html_path)
        )

        return state

    def generate_html(
            self,
            state,
            file_path
    ):

        html = f"""
        <html>

        <head>
        <title>Incident Report</title>
        </head>

        <body>

        <h1>Agentic AI Incident Report</h1>

        <h2>Summary</h2>

        <p>
        Incident ID:
        {state.incident_id}
        </p>

        <p>
        Root Cause:
        {state.root_cause}
        </p>

        <p>
        Confidence:
        {state.confidence}
        </p>

        <p>
        Selected Action:
        {state.selected_action}
        </p>

        <p>
        Healing Successful:
        {state.healing_successful}
        </p>

        <h2>Evidence</h2>

        <ul>
        {
            "".join(
                [
                    f"<li>{e}</li>"
                    for e in state.evidence
                ]
            )
        }
        </ul>

        </body>

        </html>
        """

        file_path.write_text(
            html
        )

    def generate_pdf(
            self,
            state,
            file_path
    ):

        doc = SimpleDocTemplate(
            str(file_path)
        )

        styles = (
            getSampleStyleSheet()
        )

        elements = []

        elements.append(
            Paragraph(
                "Agentic AI Incident Report",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(
                1,
                20
            )
        )

        elements.append(
            Paragraph(
                f"Incident: "
                f"{state.incident_id}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"Root Cause: "
                f"{state.root_cause}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"Action: "
                f"{state.selected_action}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"Recovered: "
                f"{state.healing_successful}",
                styles["BodyText"]
            )
        )

        doc.build(
            elements
        )

    def generate_json(
            self,
            state,
            file_path
    ):

        payload = {

            "incident_id":
                state.incident_id,

            "root_cause":
                state.root_cause,

            "confidence":
                state.confidence,

            "selected_action":
                state.selected_action,

            "healing_successful":
                state.healing_successful,

            "evidence":
                state.evidence
        }

        with open(
            file_path,
            "w"
        ) as f:

            json.dump(
                payload,
                f,
                indent=4
            )