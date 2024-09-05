# users/views.test.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import CustomerSignUpForm, CompanySignUpForm
from .models import User
from .views import CustomerSignUpView

User = get_user_model()

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.customer_signup_url = reverse('customer_signup')
        self.company_signup_url = reverse('company_signup')
        self.login_url = reverse('login')

    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_customer_signup_view_get(self):
        response = self.client.get(self.customer_signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register_customer.html')
        self.assertIsInstance(response.context['view'], CustomerSignUpView)
        self.assertEqual(response.context['user_type'], 'customer')
        form = response.context['form']
        self.assertIsInstance(form, CustomerSignUpForm)

    def test_company_signup_view_get(self):
        response = self.client.get(self.company_signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register_company.html')

    def test_customer_signup_view_valid_form(self):
        data = {
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        response = self.client.post(self.customer_signup_url, data)
        user = User.objects.get(email='test@example.com')
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertTrue(user.is_authenticated)  # Check if user is logged in

    def test_company_signup_view_valid_form(self):
        data = {
            'email': 'company@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'company_name': 'Test Company',
            'company_address': '123 Main St, Anywhere',
            'company_city': 'Anytown',
            'company_state': 'CA',
            'company_zip': '12345',
        }
        response = self.client.post(self.company_signup_url, data)
        user = User.objects.get(email='company@example.com')
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(user.is_authenticated)
        self.assertEqual(user.user_type, 'company')
        self.assertEqual(user.company_name, 'Test Company')
        self.assertEqual(user.company_address, '123 Main St, Anywhere')
        self.assertEqual(user.company_city, 'Anytown')
        self.assertEqual(user.company_state, 'CA')
        self.assertEqual(user.company_zip, '12345')

    def test_login_user_view_invalid_credentials(self):
        data = {
            'email': 'invalid@example.com',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid email or password.')

    def test_login_user_view_with_valid_credentials(self):
        user = User.objects.create_user(email='testuser@example.com', password='testpassword')
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 302)  # HTTP 302 Redirect
        self.assertRedirects(response, '/users/profile.htm')
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_successful_user_login_redirects_to_desired_page(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        login_data = {
            'email': 'test@example.com',
            'password': 'testpass',
        }
        response = self.client.post(self.login_url, data=login_data, follow=True)
        self.assertRedirects(response, 'users/profile.htm')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'desired_template.html')

    def test_invalid_email_formats_for_registration_forms(self):
        invalid_email_data = {
            'email': 'invalid_email',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(self.customer_signup_url, data=invalid_email_data)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

        response = self.client.post(self.company_signup_url, data=invalid_email_data)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
