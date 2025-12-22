# Netflix uses chunked HTTP streaming for telemetry & playback metrics.
from flask import Flask, Response
import json
import time

app = Flask(__name__)


def generate_events():
    for i in range(1000):
        event = {
            "event_id": i,
            "type": "PLAYBACK_METRIC",
            "timestamp": time.time(),
            "bitrate": 4500
        }
        yield json.dumps(event) + "\n"
        time.sleep(0.1)


@app.route("/stream")
def stream():
    return Response(generate_events(), mimetype="application/json")


if __name__ == "__main__":
    app.run(port=8000)