# -*- coding: utf-8 -*-
import math

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
i=1
while (i<=a):
    if (a%i==0) and (b%i==0):
        mdc=i
    i=i+1
print (mdc)