# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
soma=0
i=1
den=n-1
if n<0:
    n=n*(-1)
for i in range(1,n+1,1):
    soma=soma+(i/(den+1))
den=0
print('%.5f'%soma)
    


