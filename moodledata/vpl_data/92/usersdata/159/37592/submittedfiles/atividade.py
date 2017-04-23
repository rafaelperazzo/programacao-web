# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
if n<0:
    n=(-1)*n
soma=0
denominador=n
while i<=n:
    soma=soma+(i/denominador)
    denominador=denominador-1
print('S: %.5f' %soma)    

