# -*- coding: utf-8 -*-
import math
n=int(input('Informe o número de termos: '))

if n>=0:
    n=n
else:
    n=(n*(-1))

S=0
    
for termo in range (1,n+1,1):
    while n > 0 :
        S=termo/n
        n=n-1
print('%.5f'%S)



