import pytest
import subprocess
import time

@pytest.fixture(scope="session")
def http_stream_server():
    proc = subprocess.Popen(["python", "mock_servers/http_stream_server.py"])
    time.sleep(2)
    yield
    proc.terminate()


@pytest.fixture(scope="session")
def websocket_server():
    proc = subprocess.Popen(["python", "mock_servers/websocket_server.py"])
    time.sleep(2)
    yield
    proc.terminate()