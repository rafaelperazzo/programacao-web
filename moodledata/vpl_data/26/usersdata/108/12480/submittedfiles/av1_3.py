# -*- coding: utf-8 -*-
from __future__ import division
import math

n1 = int (input ('Digite um número inteiro:'))
n2 = input ('Digite um número real:')
i=1
contador1=0
contador2=1
j=1

while (i<n1):
    if (n1//i>0):
        contador1 = contador1+1
    i=i*10

print (contador1)

while (n2%10!=0):
    contador2 = contador2+1
    n2=n2*10
    
print (contador2)