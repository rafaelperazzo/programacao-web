# -*- coding: utf-8 -*-
n=int(input('digite o numero de elementos de a:'))
m=int(input('digite o numero de elementos de b:'))
listaa=[]
listab=[]
for i in range (0,n,1):
    elea=int(input('digite o elemento:'))
    listaa.append(elea)

for i in range(0,m,1):
    eleb=int(input('digite o elemento:'))
    listab.append(eleb)
    
for i in range(0,n,1) and c in range(0,m,1):
    cont1=0
    if listaa[i]==listab[c]:
        cont=cont+1

print(cont)    
