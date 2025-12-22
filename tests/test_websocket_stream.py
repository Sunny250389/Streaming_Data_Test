from streaming.clients.websocket_client import WebSocketClient
from streaming.validators.schema_validator import validate_schema


def test_websocket_stream(websocket_server):
    client = WebSocketClient("ws://localhost:8765")
    events = client.consume(max_events=5)

    for event in events:
        validate_schema(event, ["driver_id", "lat", "lng", "timestamp"])
