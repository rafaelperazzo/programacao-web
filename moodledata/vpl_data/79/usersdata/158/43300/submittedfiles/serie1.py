# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
soma=0
numer=1
for i in range(1,n+1,1):
    if i%2==0:
        soma=soma-numer/(numer**2)
    else:
        soma=soma+numer/(numer**2)
print('soma= %.5f' %S)

