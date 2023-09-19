import unittest
from aula_6 import multiplicar
from aula_6 import adicionar
from aula_6 import subtrair
from aula_6 import dividir

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar_dois_por_tres(self):
        self.assertEqual(multiplicar(2, 3), 6)

class TestAdicionar(unittest.TestCase):
    def test_adicionar_dois_por_tres(self):
        self.assertEqual(adicionar(2, 3), 5)

class TestSubtrair(unittest.TestCase):
    def test_subtrair_dois_por_tres(self):
        self.assertEqual(subtrair(2, 3), -1)

class TestDividir(unittest.TestCase):
    def test_dividir_dois_por_tres(self):
        self.assertEqual(dividir(3, 3), 1)

if __name__ == '__main__':
    unittest.main()


