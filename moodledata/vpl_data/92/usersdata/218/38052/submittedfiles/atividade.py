# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de n:'))
numerador=1
denominador=n
termo=1
if n<0:
    n=n*(-1)
for i in range(1,n+1):
    termo=numerador/denominador
    numerador=numerador+1
    denominador=denominador-1
print('%.5f'%termo)    
    
        

