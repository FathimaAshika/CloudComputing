from utils import get

def test_frontend_health():
    r = get("/")
    assert r.status_code == 200

def test_listing_service_health():
    r = get("/listing/health")
    assert r.status_code == 200

def test_inquiry_service_health():
    r = get("/inquiry/health")
    assert r.status_code == 200
