import requests

endpoint = "http://localhost:8000/api/users/"

data = {
    "email": "new12w33122u1e33ser3@example.com",
    "username": 'new1221133e333wuser3',
    "password": 'newus3er3',
}
post_response = requests.post(endpoint, json=data)
print(post_response.json())
