# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input("Digite a quantidade de termos:")
a=[]
for i in range (1,n+1,1):
    a.append(input("Digite um elemento:"))
    
j=0
b=0

for i in range (1,n+1,1):
    b=a[j]+b
    j=j+1
    
e=a[0]
d=a[n-1]
f=b/n

print(e)
print(d)
print(f)
z=0
soma=0
for i in range (1,n+1,1):
    soma=((a[z]-f)**2)+soma
    z=z+1
    
soma=(soma)*(1/(n-1))
soma=soma**(1/2)
print(soma)
    
    

