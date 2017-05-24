# -*- coding: utf-8 -*-
import math
n1=int(input('Digite um número qualquer:'))
n2=int(input('Digite um número qualquer:'))
cont=1
r1=n1%n2
while r1>0:
    r=n2%r1
    n2=r1
    r1=r
    cont=cont+1
if r>0:
    print(r)
print(cont)
