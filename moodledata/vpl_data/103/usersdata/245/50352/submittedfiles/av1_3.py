# -*- coding: utf-8 -*-
import math
n1=int(input('Digite um número qualquer:'))
n2=int(input('Digite um número qualquer:'))
cont=0
resto=n1%n2
r=1000
while r>1:
    r=n2%resto
    n2=r
    resto=r
    cont=cont+1
print(r)
print(cont)