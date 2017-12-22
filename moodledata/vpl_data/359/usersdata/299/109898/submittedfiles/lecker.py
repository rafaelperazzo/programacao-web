# -*- coding: utf-8 -*-
n=int(input('quantidade de elementos: '))
a=[]
b=[]
for i in range(0,n,1):
    a.append(int(input('elemento %d da lista a: '%[i+1])
for i in range(0,n,1):
    b.append(int(input('elemento %d da lista b: '%[i+1])
verdadea=0
for i in range(2,n,1):
    if a[i-2]<a[i-1] and a[i-1]>a[i]:
        verdadea+=1
verdadeb=0
for i in range(2,n,1):
    if b[i-2]<b[i-1] and b[i-1]>b[i]:
        verdadeb+=1
if verdadea==1:
    print('S')
else:
    print('N')
if verdadeb==1:
    print('S')
else:
    print('N')

