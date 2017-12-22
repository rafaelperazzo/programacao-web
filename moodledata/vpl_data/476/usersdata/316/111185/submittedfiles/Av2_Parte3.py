# -*- coding: utf-8 -*-
na=int(input('digite o numero de elementos da lista a: '))
nb=int(input('digite o numero de elementos da lista b: '))
a=[]
b=[]
c=[]
for i in range(0,na,1):
    a.append(int(float(input('digite um elemento de a: '))))
for i in range(0,nb,1):
    b.append(int(float(input('digite um elemento de b: '))))
for i in range(0,max(na,nb),1):
    if i in b and i in a:
        c.append(i)
print(len(c))



