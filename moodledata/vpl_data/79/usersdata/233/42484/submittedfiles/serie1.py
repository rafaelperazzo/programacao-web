# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de termos: '))
s=0
numerador=1
denominador=numerador**2
for i in range(1,n+1,1):
    if (numerador%2)==0:
        s=s-(numerador/denominador)
    else:
        s=s+(numerador/denominador)
    numerador=numerador+1
    denominador=numerador**2
 print('%.5f'%s)
        
    


