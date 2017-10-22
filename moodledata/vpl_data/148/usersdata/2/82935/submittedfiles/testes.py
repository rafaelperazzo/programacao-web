# -*- coding: utf-8 -*-

import unittest

def calcularPi(n):
    s = 0
    pi = 1
    numerador = 2
    denominador = 1
    i = 1
    while i<=n:
       s=s*(numerador/denominador)
       i = i + 1
    pi=2*s
    return (pi)

class TestAdd(unittest.TestCase):
    
    def test_add_integers(self):
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)
 

#if __name__ == '__main__':
#    unittest.main()

n=int(input('Digite a quantidade de termos:'))

resultado = calcularPi(n)
print('%.5f' %resultado)