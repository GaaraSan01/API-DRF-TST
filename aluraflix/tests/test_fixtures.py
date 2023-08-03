from aluraflix.models import Programa
from django.test import TestCase

class FixturesTestCases(TestCase):
    
    fixtures = ['programas_iniciais']

    def test_verification_get_fixtures(self):
        """Teste de carregamento de dados Iniciais"""

        programe_test = Programa.objects.get(pk=1)
        all_programe = Programa.objects.all()
        self.assertEqual(programe_test.titulo, 'Coisas bizarras')
        self.assertEqual(len(all_programe), 9)