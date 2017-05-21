# -*- coding: utf-8 -*-
import math
n=int(input('digite um numero:'))

soma=0


for numerador in range (1,n+1,1):
    if (i%2==1):
        soma=soma+(numerador/(numerador**2)
        else:
            soma=soma-(numerador/numerador**2)
    
print('%.5f' %soma)

