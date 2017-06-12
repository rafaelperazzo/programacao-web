# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('D: '))
a=[]
for i in range (0, n, 1):
    va=int(input('d: '))
    a.append(va)
for i in range (0, n, 1):
    if (a[i]%2==0):
        print(a[i])