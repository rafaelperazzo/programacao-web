# -*- coding: utf-8 -*-
import math
n1=int(input('Digite o valor do número 1: '))
n2=int(input('Digite o valor do número 2: '))
cont=0
i=0
while (n1%n2)!=0:
    resto=(n1%n2)
    cont=cont+1
    i=i+1
print(resto)
print(cont)

