from utils import post

def test_create_inquiry():
    payload = {
        "plot_id": "P123",
        "name": "John Doe",
        "email": "john@test.com",
        "message": "I am interested."
    }
    r = post("/inquiry", payload)
    assert r.status_code == 201
