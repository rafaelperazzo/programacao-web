# -*- coding: utf-8 -*-
import math
n=int(input('digite a quantidade de divisores:'))
a=int(input('digite um valor para a:'))
b=int(input('digite um valor para b:'))
for i in range (1,n+1,1):
    if (a%i)==0 or (b%i)==0:
        print(i)