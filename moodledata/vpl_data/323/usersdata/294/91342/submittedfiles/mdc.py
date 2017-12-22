# -*- coding: utf-8 -*-
import math
n1= int(input('Digite um inteiro positivo: '))
n2= int(input('Digite um inteiro positivo: '))
mdc= 1
if n1>n2:
    m= n1
else:
    m= n2
for i in range(1,m):
    if n1%i==0 and n2%i==0:
        mdc=i
print(mdc)
