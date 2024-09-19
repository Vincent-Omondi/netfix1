from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone
from users.models import Customer, Company
import datetime

User = get_user_model()

class UserManagerTestCase(TestCase):
    def test_create_user(self):
        print("\nTesting user creation...")
        user = User.objects.create_user(email='test@example.com', username='testuser', password='testpass123')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpass123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        print("User created successfully.")

    def test_create_user_without_email(self):
        print("\nTesting user creation without email...")
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', username='testuser', password='testpass123')
        print("ValueError raised as expected.")

    def test_create_superuser(self):
        print("\nTesting superuser creation...")
        admin_user = User.objects.create_superuser(email='admin@example.com', username='adminuser', password='adminpass123')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertEqual(admin_user.username, 'adminuser')
        self.assertTrue(admin_user.check_password('adminpass123'))
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        print("Superuser created successfully.")

class UserModelTestCase(TestCase):
    def test_user_creation(self):
        print("\nTesting regular user creation...")
        user = User.objects.create_user(email='user@example.com', username='regularuser', password='userpass123')
        self.assertFalse(user.is_company)
        self.assertFalse(user.is_customer)
        print("Regular user created successfully.")

    def test_unique_constraints(self):
        print("\nTesting unique constraints...")
        User.objects.create_user(email='unique@example.com', username='uniqueuser', password='pass123')
        with self.assertRaises(Exception):
            User.objects.create_user(email='unique@example.com', username='anotheruser', password='pass123')
        with self.assertRaises(Exception):
            User.objects.create_user(email='another@example.com', username='uniqueuser', password='pass123')
        print("Unique constraints working as expected.")

    def test_str_method(self):
        print("\nTesting user __str__ method...")
        user = User.objects.create_user(email='str@example.com', username='struser', password='pass123')
        self.assertEqual(str(user), 'struser')
        print("User __str__ method working correctly.")

class CustomerModelTestCase(TestCase):
    def setUp(self):
        print("\nSetting up CustomerModelTestCase...")
        self.user = User.objects.create_user(
            email='customer@test.com',
            username='customertest',
            password='testpass123'
        )

    def test_customer_creation(self):
        print("\nTesting customer creation...")
        customer = Customer.objects.create(user=self.user, birth=datetime.date(1990, 1, 1))
        self.assertEqual(customer.user, self.user)
        self.assertEqual(customer.birth, datetime.date(1990, 1, 1))
        print("Customer created successfully.")

    def test_str_method(self):
        print("\nTesting customer __str__ method...")
        customer = Customer.objects.create(user=self.user, birth=datetime.date(1990, 1, 1))
        self.assertEqual(str(customer), f"{self.user.id} - {self.user.username}")
        print("Customer __str__ method working correctly.")

    def test_age_calculation(self):
        print("\nTesting age calculation...")
        customer = Customer.objects.create(user=self.user, birth=datetime.date(1990, 1, 1))
        today = timezone.now().date()
        expected_age = today.year - 1990 - ((today.month, today.day) < (1, 1))
        self.assertEqual(customer.age(), expected_age)
        print(f"Age calculated correctly: {expected_age}")

class CompanyModelTestCase(TestCase):
    def setUp(self):
        print("\nSetting up CompanyModelTestCase...")
        self.user = User.objects.create_user(
            email='company@test.com',
            username='companytest',
            password='testpass123'
        )

    def test_company_creation(self):
        print("\nTesting company creation...")
        company = Company.objects.create(user=self.user, field='Plumbing')
        self.assertEqual(company.user, self.user)
        self.assertEqual(company.field, 'Plumbing')
        self.assertEqual(company.rating, 0)
        print("Company created successfully.")

    def test_str_method(self):
        print("\nTesting company __str__ method...")
        company = Company.objects.create(user=self.user, field='Plumbing')
        self.assertEqual(str(company), f"{self.user.id} - {self.user.username}")
        print("Company __str__ method working correctly.")

    def test_field_choices(self):
        print("\nTesting company field choices...")
        company = Company.objects.create(user=self.user, field='Plumbing')
        self.assertIn(company.field, dict(Company._meta.get_field('field').choices))

        with self.assertRaises(ValidationError):
            invalid_company = Company(user=self.user, field='Invalid Field')
            invalid_company.full_clean()
        print("Company field choices working as expected.")

    def test_rating_validation(self):
        print("\nTesting company rating validation...")
        company = Company.objects.create(user=self.user, field='Plumbing')
        
        company.rating = 5
        company.full_clean()  # Should not raise an error
        print("Rating 5 is valid.")

        company.rating = 0
        company.full_clean()  # Should not raise an error
        print("Rating 0 is valid.")

        with self.assertRaises(ValidationError):
            company.rating = 6
            company.full_clean()
        print("Rating 6 is invalid as expected.")

        with self.assertRaises(ValidationError):
            company.rating = -1
            company.full_clean()
        print("Rating -1 is invalid as expected.")

class IntegrationTestCase(TestCase):
    def test_user_customer_relationship(self):
        print("\nTesting user-customer relationship...")
        user = User.objects.create_user(email='integration@test.com', username='integrationtest', password='testpass123')
        customer = Customer.objects.create(user=user, birth=datetime.date(1990, 1, 1))
        self.assertEqual(user.customer, customer)
        self.assertEqual(customer.user, user)
        print("User-customer relationship working correctly.")

    def test_user_company_relationship(self):
        print("\nTesting user-company relationship...")
        user = User.objects.create_user(email='integration2@test.com', username='integrationtest2', password='testpass123')
        company = Company.objects.create(user=user, field='Plumbing')
        self.assertEqual(user.company, company)
        self.assertEqual(company.user, user)
        print("User-company relationship working correctly.")