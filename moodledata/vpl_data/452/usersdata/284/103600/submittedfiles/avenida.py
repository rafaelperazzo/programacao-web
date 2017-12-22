# -*- coding: utf-8 -*-
matriz=[]
m=int(input('casa na horizontal: '))
n=int(input('casa na vertical: '))
for i in range(0,m,1):
    b=[]
    for j in range(0,n,1):
        b.append(int(input('valor da casa: ')))
    matriz.append(b)
print(b)