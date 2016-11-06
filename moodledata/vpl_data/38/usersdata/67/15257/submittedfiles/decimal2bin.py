# -*- coding: utf-8 -*-
from __future__ import division

a=input("Digite o número binario:")
cont=1
b=a
c=a
k=a
g=a
while (b//10!=0):
    if b/10!=0:
        cont=cont+1
    b=b//10
j=0
z=0
for i in range (1,cont+1,1):
    g=g%10
    z=(g*(2**j))+z
    print(z)
    
    
    c=c/10
    g=c
    j=j+1
print(z)