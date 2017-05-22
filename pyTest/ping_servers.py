import requests

def test_ping_servers():
    r = requests.get("http://www.google.com")
    assert r.status_code == 200

test_ping_servers()