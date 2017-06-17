# -*- coding: utf-8 -*-
a=[]
b=[]
n=int(input('quantidade de elementos de a:'))
m=int(input('quantidade de elementos de b:'))
for i in range(0,n,1):
    x=int(input('digite o elemento de a:'))
    a.append(x)
for i in range(0,m,1):
    y=int(input('digite o elemento de b:'))
    b.append(y)
    
    
cont=0
for i in range(0,len(a),1):
    for j in range(0,len(b),1):
        if a[i]==b[j]:
            cont=cont+1

print(cont)