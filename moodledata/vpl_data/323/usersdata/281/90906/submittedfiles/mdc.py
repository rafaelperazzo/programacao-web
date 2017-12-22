# -*- coding: utf-8 -*-
import math
x = int (input('Digite um número: '))
y = int (input('Digite outro número: '))

i = 0
mdc = 0
while (i<=y) and (i<=x):
    if (x%i==0) and (y%i==0):
        mdc = i
        print(i) 
    i = i + 1
    

    




