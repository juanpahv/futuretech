from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from posts.models import Seller

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
        }

        self.seller_data = {
            'username': 'testseller',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'first_name': 'Test',
            'last_name': 'Seller',
            'email': 'seller@example.com',
            'public_name': 'TestShop',
        }

    def test_user_registration_success(self):
        # Paso 1: Accede a la página de registro.
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

        # Paso 2: Ingresa datos válidos en los campos de registro.
        response = self.client.post(reverse('signup'), data=self.user_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # Verifica que se haya creado correctamente la cuenta del usuario.
        self.assertTrue(User.objects.filter(username=self.user_data['username']).exists())

        # Paso 3: Inicia sesión con las credenciales recién creadas.
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302) 

        # Paso 4: Confirma que la autenticación sea exitosa.
        user = User.objects.get(username=self.user_data['username'])
        self.assertTrue(user.is_authenticated)

    def test_user_registration_failure(self):
        # Paso 1: Accede a la página de registro.
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

        # Paso 2: Ingresa datos inválidos en los campos de registro.
        invalid_user_data = self.user_data.copy()
        invalid_user_data['password2'] = 'differentpassword'
        response = self.client.post(reverse('signup'), data=invalid_user_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # Verifica que la cuenta del usuario no se haya creado.
        self.assertFalse(User.objects.filter(username=self.user_data['username']).exists())

    def test_seller_registration_success(self):
        # Paso 1: Accede a la página de registro de vendedor.
        response = self.client.get(reverse('signUpAsSeller'))
        self.assertEqual(response.status_code, 200)

        # Paso 2: Ingresa datos válidos en los campos de registro.
        response = self.client.post(reverse('signUpAsSeller'), data=self.seller_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # Verifica que se haya creado correctamente la cuenta del vendedor.
        self.assertTrue(User.objects.filter(username=self.seller_data['username']).exists())
        self.assertTrue(Seller.objects.filter(publicName=self.seller_data['public_name']).exists())

        # Paso 3: Inicia sesión con las credenciales recién creadas.
        response = self.client.post(reverse('login'), {'username': 'testseller', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302) 

        # Paso 4: Confirma que la autenticación sea exitosa.
        user = User.objects.get(username=self.seller_data['username'])
        self.assertTrue(user.is_authenticated)

    def test_seller_registration_failure(self):
        # Paso 1: Accede a la página de registro de vendedor.
        response = self.client.get(reverse('signUpAsSeller'))
        self.assertEqual(response.status_code, 200)

        # Paso 2: Ingresa datos inválidos en los campos de registro.
        invalid_seller_data = self.seller_data.copy()
        invalid_seller_data['password2'] = 'differentpassword'
        response = self.client.post(reverse('signUpAsSeller'), data=invalid_seller_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # Verifica que la cuenta del vendedor no se haya creado.
        self.assertFalse(User.objects.filter(username=self.seller_data['username']).exists())
        self.assertFalse(Seller.objects.filter(publicName=self.seller_data['public_name']).exists())