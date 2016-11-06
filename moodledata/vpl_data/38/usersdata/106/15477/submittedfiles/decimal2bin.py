# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite um número na base binária:')
contador = 0
a = n
numero = 0
while n>=1:
    contador = contador +1
    n= n//10
digitos=contador
b= a//(10**(contador-1))
contador = contador-1
i = digitos - 1
while i >=0:
    numero= numero + (b*(2**i))
    b= (a - ((a//(10**(contador-1)))*(10**(contador-1))))//(10**(contador-1))
    contador= contador -1
    i = i-1
print (numero)