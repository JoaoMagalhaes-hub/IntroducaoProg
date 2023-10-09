import unittest
def somar(a,b):
    return a + b

class TestSoma(unittest.TestCase):
    def teste_soma_positivos(self):
        self.assertEqual(somar(2, 3 ), 5)
    def teste_soma_negativos(self):
        self.assertEqual(somar(-1, -1 ), -2)

if __name__ == '__main__':
    unittest.main()
