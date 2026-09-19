import subprocess
import sys
import time


def start_fastapi():
    return subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "app.api.main:app",
            "--host",
            "0.0.0.0",
            "--port",
            "8000"
        ]
    )


def start_streamlit():
    return subprocess.Popen(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            "app/dashboard/streamlit_app.py",
            "--server.port",
            "8501"
        ]
    )


if __name__ == "__main__":

    api = start_fastapi()

    time.sleep(3)

    dashboard = start_streamlit()

    print(
        "\n"
        "===================================\n"
        "Agentic AI Self Healing Started\n"
        "===================================\n"
        "API:\n"
        "http://localhost:8000\n\n"
        "Dashboard:\n"
        "http://localhost:8501\n"
    )

    api.wait()
    dashboard.wait()
