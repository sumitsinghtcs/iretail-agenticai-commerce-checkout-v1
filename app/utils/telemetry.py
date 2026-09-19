import json
import time

from pathlib import Path


METRICS_DIR = Path("metrics")

METRICS_DIR.mkdir(
    exist_ok=True
)


class TelemetryManager:

    def __init__(self):

        self.metrics = []

    def start_timer(self):

        return time.time()

    def stop_timer(
            self,
            metric_name,
            start_time
    ):

        duration = (
            time.time() - start_time
        ) * 1000

        metric = {
            "metric_name": metric_name,
            "duration_ms": round(
                duration,
                2
            ),
            "timestamp": time.time()
        }

        self.metrics.append(metric)

        self.persist()

        return metric

    def persist(self):

        output = (
            METRICS_DIR /
            "metrics.json"
        )

        with open(
            output,
            "w"
        ) as f:

            json.dump(
                self.metrics,
                f,
                indent=4
            )


telemetry = TelemetryManager()