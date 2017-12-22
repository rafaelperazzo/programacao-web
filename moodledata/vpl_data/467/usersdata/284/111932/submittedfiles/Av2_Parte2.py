# -*- coding: utf-8 -*-
m=(int(input('digite a quantidade de termos de a: ')))
n=(int(input('digite a quantidade de termos de b: ')))
a=[]
b=[]
for i in range(0,m,1):
    a.append(int(input('digite o numero de a: ')))
for i in range(0,n,1):
    b.append(int(input('digite o numero de b: ')))  

for i in range(0,m,1):
    if a[i] in b[i]:
        cont=cont+1