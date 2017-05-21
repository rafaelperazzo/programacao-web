# -*- coding: utf-8 -*-
import math
n=int(input('digite n :'))
soma=0
for numerador in range(1,n+1,1):
    denominador=numerador**2
    if numerador/denominador>=0:
        soma1=soma+1/denominador
    else:
        soma2=soma-1/denominador
print('%.5f'%soma)    
    

