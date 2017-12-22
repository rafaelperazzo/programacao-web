# -*- coding: utf-8 -*-
n= int(input('Digite o numero de elementos da lista a: '))
m= int(input('Digite o número de elementos da lista b: '))
a=[]
b=[]
for i in range (0,n,1):
    a.append(int(input('Digite o elemento%d: ' %(i+1))))
for i in range (0,m,1):
    b.append(int(input('Digite o elemento%d: ' %(i+1))))
c=0
for i in range (0,n-1,1):
    for j in range (0,m-1,1):
        if a[i]==b[j]:
            c+=1
print(c)


