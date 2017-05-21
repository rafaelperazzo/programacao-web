# -*- coding: utf-8 -*-
import math
n=int(input('Digite quantidade de termos: '))
soma=0
denominador=n
for numerador in range (1,n+1,1):
    if numerador%2==1:
        soma=soma+1/denominador
    else:
        soma=soma-1/denominador
    denominador=denominador**2
print('%.5f' %soma)