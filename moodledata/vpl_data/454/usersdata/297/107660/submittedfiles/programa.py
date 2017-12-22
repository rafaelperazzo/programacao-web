# -*- coding: utf-8 -*-
c=int(input('digite o numero de elementos da lista: '))
estoquec=[]
for i in range(c):
    estoquec.append(int(input('digite o %d elemento: '%(i+1))))
cont=0
for i in range(c):
    if estoque[i]==estoque[i+1]:
        cont+=1
    elif estoque[i-1]==estoque[i]:
        cont+=1
    elif estoque[i-1]==estoque[i+1]:
        cont+=1
r=c-cont
total=r*2
print(total)
    
