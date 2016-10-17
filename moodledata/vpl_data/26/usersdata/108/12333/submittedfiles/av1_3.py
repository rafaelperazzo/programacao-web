# -*- coding: utf-8 -*-
from __future__ import division
import math

n1 = int (input ('Digite um número inteiro:'))
n2 = input ('Digite um número real:')
i=1
contador1=0
contador2=0
j=1
n=0

while (i<=n1):
    if (n%i>=0):
        contador1 = contador1+1
    i=i*10

print (contador1)

while (n<n2):
    contador2 = contador2+1
    j=j*10
    n=j*n2
    
print (contador2)