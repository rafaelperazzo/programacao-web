# -*- coding: utf-8 -*-
import math
a=int(input('Digite um numero inteiro positivo: '))
b=int(input('Digite um segundo numero inteiro positivo: '))
while(b!=0):
    resto=a%b
    a=b
    b=resto
print(a)

