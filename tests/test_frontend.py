from utils import get

def test_frontend_homepage_loads():
    r = get("/")
    assert r.status_code == 200
    assert "html" in r.text.lower()
