# tests/test_descuento.py

import unittest
import json
import sys
import os

# Asegúrate de que el módulo src esté en el path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculo_descuento import calcular_descuento

class TestCalculoDescuento(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('tests/casos_prueba.json') as f:
            cls.casos_prueba = json.load(f)

    def test_descuento(self):
        for caso in self.casos_prueba:
            input_data = caso['input']
            expected_output = caso['expected_output']
            result = calcular_descuento(input_data['precio'], input_data['es_vip'])
            self.assertEqual(result, expected_output, f"Fallo: {input_data} produjo {result} pero se esperaba {expected_output}")

if __name__ == '__main__':
    unittest.main()
