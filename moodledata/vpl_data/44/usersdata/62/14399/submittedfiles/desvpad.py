# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input("Digite o valor de n: ")
l=[]
i=0
while i<n:
    l.append(input("Digite um elemento da lista: "))
    i=i+1

soma=0
i=0
while i<n:
    soma=(soma+l[i])
    i=i+1
media=((soma)/(len(l)))
    
    

print ("%.2f"%l[0])
print ("%.2f"%l[len(l)-1])
print ("%.2f"%media)

desvio=0
i=0
soma=0
while i<n:
    soma=(l[i]-media)**2
desvio=((1/n-1)*soma)**0.5

print ("%.2f"%desvio)