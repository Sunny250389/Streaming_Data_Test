

def validate_ordering(events, key):
    values = [e[key] for e in events]
    assert values == sorted(values), "Events out of order"
