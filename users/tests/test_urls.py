from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users import views as v

class TestUrls(SimpleTestCase):
    
    def test_register_url_resolves(self):
        print("\nTesting register URL...")
        url = reverse('users:register')
        self.assertEquals(resolve(url).func, v.register)
        print("Register URL resolves correctly.")

    def test_register_company_url_resolves(self):
        print("\nTesting register company URL...")
        url = reverse('users:register_company')
        self.assertEquals(resolve(url).func.view_class, v.CompanySignUpView)
        print("Register company URL resolves correctly.")

    def test_register_customer_url_resolves(self):
        print("\nTesting register customer URL...")
        url = reverse('users:register_customer')
        self.assertEquals(resolve(url).func.view_class, v.CustomerSignUpView)
        print("Register customer URL resolves correctly.")

    def test_login_user_url_resolves(self):
        print("\nTesting login user URL...")
        url = reverse('users:login_user')
        self.assertEquals(resolve(url).func, v.loginUserView)
        print("Login user URL resolves correctly.")

    def test_profile_url_resolves(self):
        print("\nTesting profile URL...")
        url = reverse('users:profile', args=['testuser'])
        self.assertEquals(resolve(url).func, v.profile)
        print("Profile URL resolves correctly.")

    def test_url_names(self):
        print("\nTesting URL names...")
        self.assertEquals(reverse('users:register'), '/users/')
        self.assertEquals(reverse('users:register_company'), '/company/')
        self.assertEquals(reverse('users:register_customer'), '/customer/')
        self.assertEquals(reverse('users:login_user'), '/login/')
        self.assertEquals(reverse('users:profile', args=['testuser']), '/profile/testuser/')
        print("All URL names resolve to correct paths.")