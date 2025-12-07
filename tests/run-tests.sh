import requests

BASE_URL = "http://<LOAD_BALANCER_DNS>"
endpoints = ["/health", "/", "/api/v1/users", "/login"]

for ep in endpoints:
    r = requests.get(BASE_URL + ep, timeout=10)
    assert r.status_code == 200, f"{ep} returned {r.status_code}"
print("All tests passed ✔")
