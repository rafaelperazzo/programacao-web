# -*- coding: utf-8 -*-
from __future__ import division

a=input("Digite o número binario:")
cont=1
b=a
c=a
while (b//10!=0):
    if b/10!=0:
        cont=cont+1
    b=b//10
j=0
z=0
while (c%10<=a):
    c=c%10
    z=(c*(2**j))+z
    j=j+1
    
print(z)