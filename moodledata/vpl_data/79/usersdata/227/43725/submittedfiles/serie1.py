# -*- coding: utf-8 -*-
import math
n=int(input('digite um numero:'))

soma=0
denominador=n
for numerador in range (1,n+1,1):
    soma=soma+numerador/denominador
    denominador=soma*1/numerador**2
    
    
    
print('%.5f'%soma)

