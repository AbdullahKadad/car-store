from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Car

User = get_user_model()

class CarModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.car = Car.objects.create(
            buyer_id=self.user,
            model='Model X',
            brand='Brand Y',
            price=10000.00,
            is_bought=False,
            buy_time='2024-07-22'
        )

    def test_car_creation(self):
        self.assertEqual(str(self.car), 'Model X by Brand Y at $10000.0')

class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

class CarsListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        Car.objects.create(
            buyer_id=self.user,
            model='Model X',
            brand='Brand Y',
            price=10000.00,
            is_bought=False,
            buy_time='2024-07-22'
        )

    def test_cars_list_view(self):
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_list.html')
        self.assertContains(response, 'Model X')

class CarDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.car = Car.objects.create(
            buyer_id=self.user,
            model='Model X',
            brand='Brand Y',
            price=10000.00,
            is_bought=False,
            buy_time='2024-07-22'
        )

    def test_car_detail_view(self):
        response = self.client.get(reverse('car_detail', args=[self.car.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_detail.html')
        self.assertContains(response, 'Model X')

class CarCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_car_create_view(self):
        response = self.client.post(reverse('car_create'), {
            'buyer_id': self.user.id,
            'model': 'Model Y',
            'brand': 'Brand Z',
            'price': 20000.00,
            'is_bought': False,
            'buy_time': '2024-07-23'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to car_list
        self.assertTrue(Car.objects.filter(model='Model Y').exists())

class CarUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.car = Car.objects.create(
            buyer_id=self.user,
            model='Model X',
            brand='Brand Y',
            price=10000.00,
            is_bought=False,
            buy_time='2024-07-22'
        )
        self.client.login(username='testuser', password='password')

    def test_car_update_view(self):
        response = self.client.post(reverse('car_update', args=[self.car.id]), {
            'model': 'Model X Updated',
            'brand': 'Brand Y',
            'price': 11000.00,
            'is_bought': True,
            'buy_time': '2024-07-22'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to car_list
        self.car.refresh_from_db()
        self.assertEqual(self.car.model, 'Model X Updated')

class CarDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.car = Car.objects.create(
            buyer_id=self.user,
            model='Model X',
            brand='Brand Y',
            price=10000.00,
            is_bought=False,
            buy_time='2024-07-22'
        )
        self.client.login(username='testuser', password='password')

    def test_car_delete_view(self):
        response = self.client.post(reverse('car_delete', args=[self.car.id]))
        self.assertEqual(response.status_code, 302)  # Redirects to car_list
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())
