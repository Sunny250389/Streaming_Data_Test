
from streaming.clients.http_stream_client import HTTPStreamClient
from streaming.validators.schema_validator import validate_schema
from streaming.validators.business_rules import validate_playback_event


def test_http_stream(http_stream_server):
    client = HTTPStreamClient("http://localhost:8000/stream")
    events = client.consume(max_events=5)

    assert len(events) == 5

    for event in events:
        validate_schema(event, ["event_id", "type", "timestamp", "bitrate"])
        validate_playback_event(event)


def test_pass():
    assert 0 == 0