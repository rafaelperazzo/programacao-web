# -*- coding: utf-8 -*-
from __future__ import division
n=int(input("Digite um valor: "))
L=[]
x=0
somaimpar=0
contimpar=0
somapar=0
contpar=0
while x<n:
    L.append(input("Digite um número: "))
    x+=1
for i in range (0,len(L),1):
    if L[i]%2!=0:
        somaimpar=somaimpar+L[i]
        contimpar+=1
    elif L[i]%2==0:
        somapar=somapar+L[i]
        contpar+=1
        
print somaimpar
print somapar
print contimpar
print contpar
print L