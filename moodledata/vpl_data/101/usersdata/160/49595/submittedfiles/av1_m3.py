# -*- coding: utf-8 -*-
import math

m=int(input('Digite a quantidade de termos:'))
i=3
denominador=1
soma=0
prox=1

for i in range(1,m+1,1):
    soma=soma+i+(4/(denominador*prox))
    denominador+1
    prox=prox+1
    
print('%.6f'%soma)
    
