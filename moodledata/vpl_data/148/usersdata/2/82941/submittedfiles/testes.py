# -*- coding: utf-8 -*-

import unittest

def calcularPi(n):
    s = 1
    pi = 1
    numerador = 2
    denominador = 1
    i = 1
    while i<=n:
       s=s*(numerador/denominador)
       i = i + 1
       if i%2==0:
           denominador = denominador + 2
       else:
           numerador = numerador + 2
       
    pi=2*s
    return (pi)

class TestAdd(unittest.TestCase):
    
    def test_pi(self):
        result = calculaPi(1)
        self.assertEqual(result, 4)
 

#if __name__ == '__main__':
#    unittest.main()

n=int(input('Digite a quantidade de termos:'))

resultado = calcularPi(n)
print('%.5f' %resultado)