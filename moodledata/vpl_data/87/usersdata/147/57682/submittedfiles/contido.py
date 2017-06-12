# -*- coding: utf-8 -*-
n=int(input('digite n:'))
m=int(input('digite m:'))
a=[]
b=[]
cont=0
for i in range(0,n,1):
    x1=int(input('digite tamanho de a:'))
    a.append(x1)
for i in range(0,m,1):
    x2=int(input('digite tamanho de b:'))
    b.append(x2)
print(a)
print(b)
for c in range(0,len(a),1):
    for v in range(0,len(b),1):
        if a[c]==b[v]:
            cont=cont+1
print(cont)
