# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
if a<=b:
    x=a
else:
    x=b
i=1
while i<=x:
    if a%i==0 and b%i==0:
        Divisor=i
    i=i+1
print(Divisor)
    
