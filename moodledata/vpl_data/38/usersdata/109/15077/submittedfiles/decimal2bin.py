# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite um número binário')
a=0
b=n

while b>=1:
    b=b/10
    a=a+1

cont=0
for i in range (0,a,1):
    u=n%10
    c=u*(2**i)
    cont=cont+c
    c=c//10
    
print (cont)