from utils import post, get

def test_create_listing():
    payload = {
        "plot_id": "P123",
        "location": "Dubai",
        "category": "Sale",
        "price": 500000,
        "available": 1
    }
    r = post("/listing", payload)
    assert r.status_code == 201
    listing_id = r.json()["id"]

    # Verify with GET
    read = get(f"/listing/{listing_id}")
    assert read.status_code == 200
    assert read.json()["plot_id"] == "P123"


def test_get_listing():

    r = get("/listing")
    assert r.status_code == 201
    listing_id = r.json()[0]["id"]

    