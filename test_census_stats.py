import requests


def get_api_status():
    random_user_list = requests.get("https://randomuser.me/api?results=100").json()
    users_for_payload = random_user_list['results']

    r = requests.post("https://census-toy.nceng.net/prod/toy-census", json={
        "actionType": "CountByCountry",
        "top": 5,
        "users": users_for_payload

    })

    print(r.status_code, r.reason, r.json())
    if r.status_code != 200:
        return r.status_code, "error"

    return r.status_code


def test_get_api_status():
    response = get_api_status()
    assert response == 200
