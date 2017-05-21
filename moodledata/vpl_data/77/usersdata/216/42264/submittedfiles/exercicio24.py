# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
i=1
while i<=a:
    if a%i==0 and b%i==0:
        print(i)
        i=i+1