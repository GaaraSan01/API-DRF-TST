from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class AuthenticationTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('usuariotest', password='123456')

    def test_authentication_credential_user(self):
        """Função que testa a autenticação de um usuário com credenciais validas"""
        user = authenticate(username='usuariotest', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_not_authorized(self):
        """Testando requisições não autorizadas
        Ex.: Usuário anonimo tentando fazer um get.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_username_authenticate(self):
        """Testando se o usuário digitar o nome errado"""
        user = authenticate(username='testando', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_password_authenticate(self):
        """Testando se o usuário errar a senha"""
        user = authenticate(username='usuariotest', password='654321')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_is_authenticate_get_items(self):
        """Testando get com o usuário autenticado"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)