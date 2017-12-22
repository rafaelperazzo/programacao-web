# -*- coding: utf-8 -*-
n=int(input('digite o numero de elementos da lista: '))
l=[]
for x in range(0,n,1):
    l.append(int(float(input('digite um elemento da lista: ))))
    
pares=0
impares=0
for i in range(len(l):
    if l[i]%2==0:
        pares=pares+l[i]
    else:
        impares=impares+l[i]
        
contimpar=0
contpar=0
for i in range(len(l)):
    if l[i]%2==0:
        contpar=contpar+1
    else:
        contimpar=contimpar+1
print(int(float(impares)))
print(int(float(pares)))
print(contimpar)
print(contpar)
print(l)