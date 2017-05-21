# -*- coding: utf-8 -*-
import math
n=int(input('digite n :'))
soma=0
for numerador in range(1,n+1,1):
    denominador=numerador**2
    s=numerador/denominador
    soma=soma+s
print('%.5f'%soma)    
    

