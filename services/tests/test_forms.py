from django.test import TestCase
from django import forms
from users.models import Company, User
from services.models import Service, ServiceHistory
from services.forms import CreateNewService, RequestServiceForm

class CreateNewServiceFormTest(TestCase):

    def setUp(self):
        print("\nSetting up necessary test data for CreateNewServiceForm tests...")
        self.company_user = User.objects.create_user(username='testcompany', email='company@test.com', password='pass123')
        self.company = Company.objects.create(user=self.company_user, field='Carpentry')

    def test_form_initialization_with_company(self):
        print("\nTesting form initialization and placeholder setup when company is provided...")
        form = CreateNewService(company=self.company)
        
        # Test field placeholders
        self.assertEqual(form.fields['name'].widget.attrs['placeholder'], 'Enter Service Name')
        self.assertEqual(form.fields['description'].widget.attrs['placeholder'], 'Enter Description')
        self.assertEqual(form.fields['price_hour'].widget.attrs['placeholder'], 'Enter Price per Hour')
        self.assertEqual(form.fields['name'].widget.attrs['autocomplete'], 'off')

        # Test field choices based on company field
        self.assertEqual(form.fields['field'].choices, [('Carpentry', 'Carpentry')])

    def test_form_initialization_with_all_in_one_company(self):
        print("\nTesting form field choices when company field is 'All in One'...")
        
        # Create a new user for the 'All in One' company
        new_company_user = User.objects.create_user(username='allinonecompany', email='allinone@test.com', password='pass123')
        
        # Create a new company for this new user
        company_all_in_one = Company.objects.create(user=new_company_user, field='All in One')
        
        form = CreateNewService(company=company_all_in_one)

        # When the company's field is 'All in One', all choices should be available
        self.assertEqual(form.fields['field'].choices, Service._meta.get_field('field').choices)


    def test_form_validation(self):
        print("\nTesting form validation with valid and invalid data...")
        valid_data = {
            'name': 'New Service',
            'description': 'A description of the service',
            'price_hour': 100.00,
            'field': 'Carpentry'
        }
        form = CreateNewService(data=valid_data, company=self.company)
        self.assertTrue(form.is_valid())  # The form should be valid with correct data

        invalid_data = {
            'name': '',  # Missing required field
            'description': 'A description',
            'price_hour': 100.00,
            'field': 'Carpentry'
        }
        form = CreateNewService(data=invalid_data, company=self.company)
        self.assertFalse(form.is_valid())  # The form should not be valid

class RequestServiceFormTest(TestCase):

    def setUp(self):
        print("\nSetting up necessary test data for RequestServiceForm tests...")
        self.company_user = User.objects.create_user(username='testcompany', email='company@test.com', password='pass123')
        self.company = Company.objects.create(user=self.company_user, field='Carpentry')
        self.service = Service.objects.create(
            company=self.company,
            name='Woodworking',
            description='Custom wood furniture',
            price_hour=50.00,
            field='Carpentry'
        )

    def test_form_initialization(self):
        print("\nTesting initialization of the RequestServiceForm...")
        form = RequestServiceForm()
        
        # Test placeholder for fields
        self.assertEqual(form.fields['address'].widget.attrs['placeholder'], 'Enter service address')
        self.assertEqual(form.fields['service_time'].widget.attrs['placeholder'], 'Enter service time in hours')

    def test_form_validation(self):
        print("\nTesting form validation for RequestServiceForm...")
        valid_data = {
            'address': '123 Main St',
            'service_time': 3
        }
        form = RequestServiceForm(data=valid_data)
        self.assertTrue(form.is_valid())  # Form should be valid with correct data

        invalid_data = {
            'address': '',  # Missing required address
            'service_time': 3
        }
        form = RequestServiceForm(data=invalid_data)
        self.assertFalse(form.is_valid())  # Form should not be valid with missing address

        invalid_time_data = {
            'address': '123 Main St',
            'service_time': 0  # Invalid service time (less than minimum value)
        }
        form = RequestServiceForm(data=invalid_time_data)
        self.assertFalse(form.is_valid())  # Form should not be valid with invalid service time
