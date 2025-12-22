from websocket import create_connection
import json


class WebSocketClient:
    def __init__(self, url):
        self.url = url

    def consume(self, max_events=5):
        ws = create_connection(self.url)
        events = []

        for _ in range(max_events):
            msg = ws.recv()
            events.append(json.loads(msg))

        ws.close()
        return events
