def validate_schema(event, required_fields):
    for field in required_fields:
        assert field in event, f"Missing field: {field}"

