import pytest
from streaming.clients.http_stream_client import HTTPStreamClient


def test_stream_disconnect():
    client = HTTPStreamClient("http://localhost:9999/stream")
    with pytest.raises(Exception):
        client.consume()
