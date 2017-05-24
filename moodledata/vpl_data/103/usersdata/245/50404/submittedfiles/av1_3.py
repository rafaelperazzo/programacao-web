# -*- coding: utf-8 -*-
import math
n1=int(input('Digite um número qualquer:'))
n2=int(input('Digite um número qualquer:'))
cont=0
r1=n1%n2
while r>0:
    r=n2%r1
    n2=r1
    r1=r
    cont=cont+1
print(cont)