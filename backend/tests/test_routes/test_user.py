def test_create_user(client):
    data={"email": "cp@gmail.com", "password": "secretpassword"}
    response = client.post("/users/", json=data)
    assert response.status_code == 201
    assert response.json()["email"] == "cp@gmail.com"