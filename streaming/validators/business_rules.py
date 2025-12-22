
def validate_playback_event(event):
    assert event["bitrate"] > 0
    assert event["type"] == "PLAYBACK_METRIC"

