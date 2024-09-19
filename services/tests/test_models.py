# services/tests/tests_models.py
from django.test import TestCase
from django.core.exceptions import ValidationError
from users.models import Company, Customer, User
from services.models import Service, ServiceHistory

class ServiceModelTest(TestCase):

    def setUp(self):
        print("\nSetting up the necessary test data for the Service model tests...")
        self.company_user = User.objects.create_user(username='testcompany', email='company@test.com', password='pass123')
        self.company = Company.objects.create(user=self.company_user, field='Carpentry')
        self.service = Service.objects.create(
            company=self.company,
            name='Woodworking',
            description='Custom wood furniture',
            price_hour=50.00,
            field='Carpentry'
        )
    
    def test_service_creation(self):
        print("\nTesting service creation with valid data (name and price_hour)...")
        self.assertEqual(self.service.name, 'Woodworking')
        self.assertEqual(self.service.price_hour, 50.00)
    
    def test_service_invalid_price(self):
        print("\nTesting service creation with an invalid price. Should raise ValidationError...")
        with self.assertRaises(ValidationError):
            Service.objects.create(
                company=self.company,
                name='Invalid Price',
                description='Price is not valid',
                price_hour='invalid_price',
                field='Carpentry'
            )
    
    def test_service_rating(self):
        print("\nTesting service rating with valid and invalid values...")
        self.service.rating = 4.5
        self.service.full_clean()  # This triggers validation
        self.assertEqual(self.service.rating, 4.5)

        self.service.rating = 6  # Invalid rating
        with self.assertRaises(ValidationError):
            self.service.full_clean()
    
    def test_service_str(self):
        print("\nTesting the string representation of the Service model...")
        self.assertEqual(str(self.service), 'Woodworking')


class ServiceHistoryModelTest(TestCase):

    def setUp(self):
        print("\nSetting up the necessary test data for the ServiceHistory model tests...")
        self.company_user = User.objects.create_user(username='testcompany', email='company@test.com', password='pass123')
        self.company = Company.objects.create(user=self.company_user, field='Carpentry')
        self.service = Service.objects.create(
            company=self.company,
            name='Woodworking',
            description='Custom wood furniture',
            price_hour=50.00,
            field='Carpentry'
        )
        
        self.customer_user = User.objects.create_user(username='testcustomer', email='customer@test.com', password='pass123')
        self.customer = Customer.objects.create(user=self.customer_user, birth='1990-01-01')
        
        self.service_history = ServiceHistory.objects.create(
            service=self.service,
            customer=self.customer,
            price=100.00,
            address='123 Main St',
            service_time=2
        )
    
    def test_service_history_creation(self):
        print("\nTesting ServiceHistory creation with valid data (price)...")
        self.assertEqual(self.service_history.price, 100.00)
    
    def test_service_history_str(self):
        print("\nTesting the string representation of the ServiceHistory model...")
        self.assertEqual(str(self.service_history), 'testcustomer - Woodworking')

    def test_service_history_rating(self):
        print("\nTesting ServiceHistory rating with valid and invalid values...")
        self.service_history.rating = 5.0
        self.service_history.full_clean()  # This triggers the model validation
        self.assertEqual(self.service_history.rating, 5.0)

        self.service_history.rating = 6  # Invalid rating
        with self.assertRaises(ValidationError):
            self.service_history.full_clean()
