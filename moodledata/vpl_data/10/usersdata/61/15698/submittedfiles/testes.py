# -*- coding: utf-8 -*-
from __future__ import division
import math 
n=int(input('Digite um valor: '))
L=[]
x=0
soma=0
cont=0
soma2=0
cont2=0
while x<n:
    L.append(input("Digite um número: "))
    x=x+1
for i in range (0,len(L),1):
    if L[i]%2!=0:
        soma=soma+L[i]
        cont+=1
    elif L[i]%2==0:
        soma2=soma+L[i]
        cont2+=1
    
print L
print soma
print cont
print soma2
print cont2



    
    
    

    
