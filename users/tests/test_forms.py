# users/tests/test_forms.py
from django.test import TestCase
from django.core.exceptions import ValidationError
from users.forms import CustomerSignUpForm, CompanySignUpForm, UserLoginForm
from users.models import User, Customer, Company
from datetime import date

class TestForms(TestCase):

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }

    def test_customer_signup_form_valid_data(self):
        print("\nTesting CustomerSignUpForm with valid data...")
        form = CustomerSignUpForm(data={
            **self.user_data,
            'birth': '1990-01-01'
        })
        self.assertTrue(form.is_valid())
        print("CustomerSignUpForm is valid with correct data.")

    def test_customer_signup_form_invalid_data(self):
        print("\nTesting CustomerSignUpForm with invalid data...")
        form = CustomerSignUpForm(data={
            **self.user_data,
            'birth': 'invalid-date'
        })
        self.assertFalse(form.is_valid())
        print("CustomerSignUpForm is invalid with incorrect date.")

    def test_customer_signup_form_save(self):
        print("\nTesting CustomerSignUpForm save method...")
        form = CustomerSignUpForm(data={
            **self.user_data,
            'birth': '1990-01-01'
        })
        user = form.save()
        self.assertTrue(user.is_customer)
        self.assertEqual(user.customer.birth, date(1990, 1, 1))
        print("CustomerSignUpForm save method works correctly.")

    def test_company_signup_form_valid_data(self):
        print("\nTesting CompanySignUpForm with valid data...")
        form = CompanySignUpForm(data={
            **self.user_data,
            'field_of_work': 'Plumbing'
        })
        self.assertTrue(form.is_valid())
        print("CompanySignUpForm is valid with correct data.")

    def test_company_signup_form_invalid_data(self):
        print("\nTesting CompanySignUpForm with invalid data...")
        form = CompanySignUpForm(data={
            **self.user_data,
            'field_of_work': 'InvalidField'
        })
        self.assertFalse(form.is_valid())
        print("CompanySignUpForm is invalid with incorrect field of work.")

    def test_company_signup_form_save(self):
        print("\nTesting CompanySignUpForm save method...")
        form = CompanySignUpForm(data={
            **self.user_data,
            'field_of_work': 'Plumbing'
        })
        user = form.save()
        self.assertTrue(user.is_company)
        self.assertEqual(user.company.field, 'Plumbing')
        print("CompanySignUpForm save method works correctly.")

    def test_user_login_form(self):
        print("\nTesting UserLoginForm...")
        form = UserLoginForm(data={
            'email': 'test@example.com',
            'password': 'testpassword123'
        })
        self.assertTrue(form.is_valid())
        print("UserLoginForm is valid with correct data.")

    def test_validate_email(self):
        print("\nTesting email validation...")
        User.objects.create_user(username='existinguser', email='existing@example.com', password='testpass123')
        
        form = CustomerSignUpForm(data={
            **self.user_data,
            'email': 'existing@example.com',
            'birth': '1990-01-01'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        print("Email validation correctly detects existing email.")

    def test_date_input_widget(self):
        print("\nTesting DateInput widget...")
        form = CustomerSignUpForm()
        self.assertEqual(form.fields['birth'].widget.input_type, 'date')
        print("DateInput widget is correctly set for birth field.")

    def test_company_field_choices(self):
        print("\nTesting company field choices...")
        form = CompanySignUpForm()
        self.assertEqual(len(form.fields['field_of_work'].choices), 12) 
        self.assertIn(('Plumbing', 'Plumbing'), form.fields['field_of_work'].choices)
        print("Company field choices are correctly set.")