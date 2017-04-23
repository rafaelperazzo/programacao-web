# -*- coding: utf-8 -*-
import math
n=int(input('digite um valor para n:'))
if n<0:
    n=n*(-1)
S=0
numerador=1
denominador=n

for numerador in range (1,n+1,1):
    S=S+numerador/denominador
    denominador=denominador-1
print('%.5f' %S)



