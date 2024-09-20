# main/test_views.py
from django.test import TestCase
from django.urls import reverse
from services.models import Service, ServiceHistory
from django.contrib.auth import get_user_model
from users.models import Company

class HomeViewTest(TestCase):

    def setUp(self):
        # Get the custom user model
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',  # Include the required email
            password='12345'
        )

        # Adjust the Company creation based on actual fields
        self.company = Company.objects.create(
            user=self.user,  # Assuming Company has a ForeignKey to the user
            company_name='Test Company',  # Replace with actual field names
            location='123 Company St'  # Replace with actual field names
        )

        # Create some service objects linked to the company
        self.service1 = Service.objects.create(
            name="Service 1", 
            company=self.company, 
            description="Service 1 description", 
            price_hour=10.00, 
            field="Plumbing"
        )
        self.service2 = Service.objects.create(
            name="Service 2", 
            company=self.company, 
            description="Service 2 description", 
            price_hour=20.00, 
            field="Electricity"
        )

        # Create service history entries
        self.history1 = ServiceHistory.objects.create(
            service=self.service1, 
            customer_id=1, 
            price=100, 
            address="123 Street", 
            service_time=2
        )
        self.history2 = ServiceHistory.objects.create(
            service=self.service2, 
            customer_id=1, 
            price=200, 
            address="456 Street", 
            service_time=3
        )


class LogoutViewTest(TestCase):

    def setUp(self):
        # Use the custom user model
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',  # Include email
            password='12345'
        )
    
    def test_logout_view_logs_out_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('main:logout'))  # Updated with 'main' namespace
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/logout.html')
        # Check user is logged out
        response = self.client.get(reverse('main:home'))  # Updated with 'main' namespace
        self.assertNotIn('_auth_user_id', self.client.session)
    
    def test_logout_view_no_user_logged_in(self):
        response = self.client.get(reverse('main:logout'))  # Updated with 'main' namespace
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/logout.html')
