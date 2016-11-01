# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
n=input("Digite o valor de n: ")
l=[]
i=0
while i<n:
    l.append(input("Digite um elemento da lista: "))
    i=i+1

soma=0
while i<n:
    soma=(soma+l[i])
    i=i+1
media=((soma)/(len(l)))
    
    

print (l[0])
print (l[len(l)-1])
print media
print (l)