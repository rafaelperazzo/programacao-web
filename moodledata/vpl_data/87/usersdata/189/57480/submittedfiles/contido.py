# -*- coding: utf-8 -*-
x=int(input('quantidade de elementos de a:'))
y=int(input('quantidade de elementos de b:'))
a=[]
b=[]
cont=0
for i in range(0,x,1):
    t1=int(input('digite tamanho de a:'))
    a.append(t1)
for j in range(0,y,1):
    t2=int(input('digite tamanho de b:'))
    b.appen(t2)
print(a)
print(b)
for t in range(0,len(a),1):
    for q in range(0,len(b),1):
        if a[t]==b[q]:
            cont=cont+1
print(cont)

