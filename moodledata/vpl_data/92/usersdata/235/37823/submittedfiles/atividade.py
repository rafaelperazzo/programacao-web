# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de n:'))
if n<0:
    n*(-1)
numerador=0
denominador=n
soma=0
cont=1
while cont<=n:
    soma=soma+(cont/denominador)
    cont=cont+1
    denominador=n-1
print('%.5f' %soma)

