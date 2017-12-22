# -*- coding: utf-8 -*-
c=int(input('digite o numero de elementos da lista: '))
estoquec=[]
for i in range(c):
    estoquec.append(int(input('digite o %d elemento: '%(i+1))))
cont=0
for i in range(1,c-1,1):
    if estoquec[i]==estoquec[i+1]:
        cont+=1
    elif estoquec[i-1]==estoquec[i]:
        cont+=1
    elif estoquec[i-1]==estoquec[i+1]:
        cont+=1
r=c-cont
total=r*2
print(total)
    
