# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
if n<0:
    n*(-1)
soma=0
i=1
den=n
for i in range(1,n+1,1):
    soma=soma+(i/(den+n-i+1))
    den=den+1
print('5.5f'%soma)
    


