import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_list():
    FAQ.objects.create(question="Test Question", answer="Test Answer")
    client = APIClient()
    url = reverse("faq-list")
    response = client.get(url)
    assert response.status_code == 200
