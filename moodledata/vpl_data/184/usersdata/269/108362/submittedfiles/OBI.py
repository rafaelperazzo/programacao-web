# -*- coding: utf-8 -*-
n=int(input('digite: '))
cont=0
p=int(input('digite: '))
for i in range(0,n,1):
    x=int(input('digite: '))
    y=int(input('digite: '))
    if (x+y) >= p:
        cont=cont+1
print(cont)        