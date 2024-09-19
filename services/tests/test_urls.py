
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from services import views as v

class TestUrls(SimpleTestCase):
    
    def test_services_list_url_resolves(self):
        print("\nTesting services list URL...")
        url = reverse('services:services_list')
        self.assertEquals(resolve(url).func, v.service_list)
        print("Services list URL resolves correctly.")

    def test_services_create_url_resolves(self):
        print("\nTesting services create URL...")
        url = reverse('services:services_create')
        self.assertEquals(resolve(url).func, v.services_create)
        print("Services create URL resolves correctly.")

    def test_index_url_resolves(self):
        print("\nTesting index URL...")
        url = reverse('services:index', args=[1])
        self.assertEquals(resolve(url).func, v.index)
        print("Index URL resolves correctly.")

    def test_request_service_url_resolves(self):
        print("\nTesting request service URL...")
        url = reverse('services:request_service', args=[1])
        self.assertEquals(resolve(url).func, v.request_service)
        print("Request service URL resolves correctly.")

    def test_service_field_url_resolves(self):
        print("\nTesting service field URL...")
        url = reverse('services:services_field', args=['plumbing'])
        self.assertEquals(resolve(url).func, v.service_field)
        print("Service field URL resolves correctly.")

    def test_service_detail_or_field_url_resolves(self):
        print("\nTesting service detail or field URL...")
        url = reverse('services:detail_or_field', args=['1'])
        self.assertEquals(resolve(url).func, v.service_detail_or_field)
        print("Service detail or field URL resolves correctly.")

    def test_service_detail_url_resolves(self):
        print("\nTesting service detail URL...")
        url = reverse('services:detail', args=[1])
        self.assertEquals(resolve(url).func, v.service_detail_or_field)
        print("Service detail URL resolves correctly.")

    def test_profile_url_resolves(self):
        print("\nTesting profile URL...")
        url = reverse('services:profile', args=['testuser'])
        self.assertEquals(resolve(url).func, v.profile)
        print("Profile URL resolves correctly.")

    def test_delete_service_url_resolves(self):
        print("\nTesting delete service URL...")
        url = reverse('services:delete_service', args=[1])
        self.assertEquals(resolve(url).func, v.delete_service)
        print("Delete service URL resolves correctly.")

    def test_rate_service_url_resolves(self):
        print("\nTesting rate service URL...")
        url = reverse('services:rate_service', args=[1])
        self.assertEquals(resolve(url).func, v.rate_service)
        print("Rate service URL resolves correctly.")

    def test_url_names(self):
        print("\nTesting URL names...")
        self.assertEquals(reverse('services:services_list'), '/services/')
        self.assertEquals(reverse('services:services_create'), '/services/create/')
        self.assertEquals(reverse('services:index', args=[1]), '/services/1')
        self.assertEquals(reverse('services:request_service', args=[1]), '/services/1/request_service/')
        self.assertEquals(reverse('services:services_field', args=['plumbing']), '/services/field/plumbing/')
        self.assertEquals(reverse('services:detail_or_field', args=['1']), '/services/1/')
        self.assertEquals(reverse('services:detail', args=[1]), '/services/detail/1/')
        self.assertEquals(reverse('services:profile', args=['testuser']), '/services/profile/testuser/')
        self.assertEquals(reverse('services:delete_service', args=[1]), '/services/delete/1/')
        self.assertEquals(reverse('services:rate_service', args=[1]), '/services/1/rate/')
        print("All URL names resolve to correct paths.")