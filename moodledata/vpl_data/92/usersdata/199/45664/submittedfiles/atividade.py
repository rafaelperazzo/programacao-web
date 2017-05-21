# -*- coding: utf-8 -*-
import math
n=int(input('Digite o Valor: '))
if n<0:
    n=n*(-1)

soma=0
den=n
for numerador in range (1,n+1,1):
    soma=soma+numerador/den
    den=den-1
print('%.5f'%soma)