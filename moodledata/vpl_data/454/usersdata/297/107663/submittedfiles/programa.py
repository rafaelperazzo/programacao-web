# -*- coding: utf-8 -*-
c=int(input('digite o numero de elementos da lista: '))
estoque=[]
for i in range(c):
    estoque.append(int(input('digite o %d elemento: '%(i+1))))
cont=0
for i in range(1,c-1,1):
    if estoque[i]==estoque[i+1]:
        cont+=1
    elif estoque[i-1]==estoque[i]:
        cont+=1
    elif estoque[i-1]==estoque[i+1]:
        cont+=1
r=c-cont
total=r*2
print(total)
    
