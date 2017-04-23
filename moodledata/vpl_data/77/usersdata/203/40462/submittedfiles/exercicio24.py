# -*- coding: utf-8 -*-
import math
n1=int(input('digite o primeiro valor: '))
n2=int(input('digite o segundo valor: '))
for i in range (2,n1+1,1):
    if n1%i==0 and n2%i==0:
        print(i)