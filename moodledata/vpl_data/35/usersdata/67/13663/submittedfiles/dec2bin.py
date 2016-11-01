# -*- coding: utf-8 -*-
from __future__ import division

p=input("Digite o valor do primeiro número:")
q=input("Digite o valor do segundo número:")
cont=1
a=q
b=q
while (a//10!=0):
    if a//10!=0:
        cont=cont+1
    a=a//10
    
for i in range (1,cont+1,1):
    if b//10==p:
        print("S")
    b=b//10
    
if q-(q-1)==p or q-(q-2)==p or q-(q-3)==p or q-(q-4)==p or q-(q-5)==p or q-(q-6)==p or q-(q-7)==p or q-(q-8)==p or q-(q-9)==p:
    print ("S")
    



    