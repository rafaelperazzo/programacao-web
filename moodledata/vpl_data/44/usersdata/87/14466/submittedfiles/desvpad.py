# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n=int(input("digite valor de n:"))
a=[]
media=0
i=0
for i in range (0,n,1):
    a.append(input("digite elemento:"))
    media=media + a[i]
m=media/(len(a))
print("%.2f"%a[0])
print("%.2f"%a[n-1])
print("%.2f"%m)

z=0
soma=0
for i in range(1,n+1,1):
    soma=((a[z]-media)**2)+soma
    z = z+1
    
soma=(soma)*(1/(n-1))
soma=soma**(1/2)
print("%.2f"%(soma))