# -*- coding: utf-8 -*-
import math
n1=int(input('Digite o valor do número 1: '))
n2=int(input('Digite o valor do número 2: '))
cont=1
while n1%n2!=0:
    resto=n1%n2
    cont=cont+1
    n1=n2
    n2=resto

print(resto)
print(cont)

