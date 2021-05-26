
from django.test import TestCase
from django.urls import reverse


class ViewsTestCase(TestCase):

    def test_index_loads_properly(self):
        url = reverse('social_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_loads_properly(self):
        url = reverse('social_login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_signup_loads_properly(self):
        url = reverse('social_signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)