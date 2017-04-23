# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
soma=0
i=1
den=0
if n<0:
    n=n*(-1)
for i in range(1,n+1,1):
    soma=soma+(i/(den+n-1+1))
den=1
print('%.5f'%soma)
    


