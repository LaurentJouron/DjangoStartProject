from django.urls import reverse


def test_my_website_is_online(client):
    response = client.get(reverse("home"))
    assert response.status_code == 200
