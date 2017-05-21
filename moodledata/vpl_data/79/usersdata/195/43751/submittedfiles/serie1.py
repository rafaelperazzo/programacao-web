# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
soma=0
denominador=1
numerador=1
for i in range (1,n+1,1):
    x=numerador/numerador*numerador
    if i%2!=0:
        soma=soma+x
    else:
        soma=soma-x
print('s: %.5f'%soma)    
