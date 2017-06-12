# -*- coding: utf-8 -*-
n=int(input('digite n: '))
m=int(input('digite m: '))
l1=[]
l2=[]
c=0
for i in range(0,n,1):
    valor1=int(input('digite v1: '))
    l1.append(valor1)
for i in range(0,m,1):
    valor2=int(input('digite v2: '))
    l2.append(valor2)
for x in range(0,len(l1),1):
    for y in range(0,len(l2),1):
        if l1[x]==l2[y]:
            c=c+1
print(c)            

