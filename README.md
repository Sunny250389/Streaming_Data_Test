# Streaming_Data_Test
    A reusable streaming-testing framework design with mock streaming server

## Content:
    1. Architecture & Principles
    2. Repo Structure
    3. Mock Streaming servers (HTTP + WebSocket)
    4. Pytest fixtures & streaming tests
    5. Netflix / Uber style patterns
    6. Advanced features used by top companies
    7. CI/CD integration strategy


### 1. Core Design Principles
    This framework is built on real streaming system constraints, not toy examples.
    
    Design goals:
    - Deterministic tests for infinite streams
    - Time-bounded & message-bounded execution
    - Schema + business validation
    - Resilience testing (disconnects, retries)
    - Observability (metrics, lag, latency)
    - Environment-agnostic (local, CI, prod-like)

### 2. Repository Structure
    pytest-streaming-framework/
    │
    ├── streaming/
    │   ├── clients/
    │   │   ├── http_stream_client.py
    │   │   ├── websocket_client.py
    │   │   └── kafka_client.py
    │   │
    │   ├── validators/
    │   │   ├── schema_validator.py
    │   │   ├── business_rules.py
    │   │   └── ordering_validator.py
    │   │
    │   ├── metrics/
    │   │   ├── latency.py
    │   │   └── throughput.py
    │   │
    │   ├── utils/
    │   │   ├── timers.py
    │   │   └── retry.py
    │
    ├── mock_servers/
    │   ├── http_stream_server.py
    │   ├── websocket_server.py
    │   └── event_generator.py
    │
    ├── tests/
    │   ├── test_http_stream.py
    │   ├── test_websocket_stream.py
    │   └── test_resilience.py
    │
    ├── conftest.py
    ├── requirements.txt
    ├── pytest.ini
    └── README.md
