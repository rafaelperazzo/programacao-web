# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
cont=0
for i in range (b,a+1,1):
    if (a%i==0) and (b%i==0):
        cont=cont+1
print(cont)