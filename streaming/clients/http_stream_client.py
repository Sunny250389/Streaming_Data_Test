import requests
import json


class HTTPStreamClient:
    def __init__(self, url):
        self.url = url

    def consume(self, max_events=10):
        response = requests.get(self.url, stream=True, timeout=10)
        response.raise_for_status()

        events = []
        for line in response.iter_lines():
            if line:
                events.append(json.loads(line))
            if len(events) >= max_events:
                break
        return events
