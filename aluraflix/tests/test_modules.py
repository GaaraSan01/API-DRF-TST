from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo= 'Filme de test',
            data_lancamento='2003-07-04',
        )

    def test_verifica_atributos_do_programa(self):
        """Teste que verifica os atributos de valores default do programa"""
        self.assertEqual(self.programa.titulo, 'Filme de test')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.data_lancamento, '2003-07-04')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)