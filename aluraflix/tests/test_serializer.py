from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class SerializersTestModelCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo= 'Filme de test',
            data_lancamento='2003-07-04',
            tipo='F',
            likes=20549,
            dislikes=134
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_serializer_camp_programe(self):
        """Testando os campos do Serilizers"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

    def test_serializer_cont_programe(self):
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)