# -*- coding: utf-8 -*-
import math
n1=int(input('digite o primeiro valor: '))
n2=int(input('digite o segundo valor: '))
i=1
while n1%i==0 and n2%i==0:
    i=i+1
print(i)