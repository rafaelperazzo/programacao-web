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

c=c/10
print(c)
