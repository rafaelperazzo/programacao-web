# -*- coding: utf-8 -*-
import math
x=int(input('Digite um número: '))
y=int(input('Digite outro número: '))
mdc=1
i=2
while(i<=x):
    if (x%i)==0 and (y%i)==0:
        mdc=i
        i=i+1

print(mdc)
        
