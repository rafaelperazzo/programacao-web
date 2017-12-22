# -*- coding: utf-8 -*-
import math
n1=int(input('Digite um numero aqui: ')
n2=int(input('Digite um numero aqui: ')
mdc=1
if n1>n2:
    x=n1
else:
    x=n2
for i in range (1,x):
    if n1%i==0 and n2%i==0:
        mdc=i
print mdc 
    
