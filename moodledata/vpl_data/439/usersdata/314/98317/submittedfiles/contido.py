# -*- coding: utf-8 -*-



n=int(input('Digite n: '))
m=int(input('Digite m: '))
a=[]
b=[]
for i in range(0,n,1):
    a.append(int(input('Digite elementos de a: ')))
for j in range(0,m,1):
    b.append(int(input('Digite ementos de b: ')))

print(set(a).intersection(b))

    