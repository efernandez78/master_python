import unittest
from compara import *

class test_compara(unittest.TestCase):
    def test1(self):
        resultado=compara_numero(4,3)
        self.assertEqual(resultado,"a es mayor que b")
    def test2(self):
        resultado=compara_numero(3,3)
        self.assertEqual(resultado,"a es igual a b")
    def test3(self):
        resultado=compara_numero(3,4)
        self.assertEqual(resultado,"a es menor que b")
    def test4(self):
        resultado=compara_cadena("Hola","Hola")
        self.assertTrue(resultado)
    def test5(self):
        resultado=compara_cadena("Hola","Adios")
        self.assertFalse(resultado)
    def test6(self):
        with self.assertRaises(TypeError):
            resultado=compara_numero("H",4)
    def test7(self):
        with self.assertRaises(TypeError):
            resultado=compara_numero("H",4)

if __name__=='__main__':
    unittest.main()
