# -*- coding: utf-8 -*-
import math

a = int(input('Digite o primeiro número: '))
b = int(input('DDigite o segundo número: '))
i=a
while a%i!=0 and b%i!=0:
    i=i-1
print (i)