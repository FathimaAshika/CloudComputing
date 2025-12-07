import os
import requests

BASE_URL = os.getenv("BASE_URL")
POSTHOG_API = os.getenv("POSTHOG_API")
POSTHOG_KEY = os.getenv("POSTHOG_KEY")

def get(url):
    return requests.get(f"{BASE_URL}{url}")

def post(url, payload):
    return requests.post(f"{BASE_URL}{url}", json=payload)

def fetch_posthog_events(event_name):
    return requests.get(
        f"{POSTHOG_API}/api/events",
        params={"event": event_name},
        headers={"Authorization": f"Bearer {POSTHOG_KEY}"}
    )
