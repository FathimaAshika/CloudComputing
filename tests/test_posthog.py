import time
from utils import fetch_posthog_events

def test_posthog_pageview_event():
    # Wait for event ingestion
    time.sleep(5)

    events = fetch_posthog_events("$pageview")
    assert events.status_code == 200
    assert len(events.json()["results"]) > 0
