# -*- coding: utf-8 -*-
import math
a=int(input('Digite a: '))
b=int(input('Digite b: '))
cont=0
for i in range(1,a+b,1):
    if a%i==0 and b%i==0:
        cont=i
    i=i+1
print(cont)