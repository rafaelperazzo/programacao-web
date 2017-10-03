# -*- coding: utf-8 -*-
import math

n=int(input('Digite o valor de n:'))

denominador=1
numerador=1
S=0

for termo in range (1,n+1,1):
    if termo%2==0:
        S=S-numerador/(denominador**2)
    else:
        S=S+numerador/(denominador**2)
    numerador=numerador+1
    denominador=denominador+1
print(S)