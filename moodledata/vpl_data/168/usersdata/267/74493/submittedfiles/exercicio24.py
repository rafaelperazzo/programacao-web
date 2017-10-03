# -*- coding: utf-8 -*-
import math

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
i=a
while (i>0):
    if (a%i==0) and (b%i==0):
        print (i)
        i=0
    else:
        i=i-1
