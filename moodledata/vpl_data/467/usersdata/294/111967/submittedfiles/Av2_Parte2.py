# -*- coding: utf-8 -*-
n= int(input('Digite a quantidade de elementos de a: '))
m= int(input('Digite a quantidade de elementos de b: '))
a=[]
b=[]
for i in range (0,n,1):
    a.append(int(input('Digite o elemento %d de a: ' %(i+1))))
for i in range (0,m,1):
    b.append(int(input('Digite o elemento %d de b: ' %(i+1))))
c=0
for i in range (0,n,1):
    if b[i] in a:
        c+=1
print(c)

