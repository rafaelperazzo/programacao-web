# -*- coding: utf-8 -*-
m=int(input('digite a ordem da matriz: '))
lista=[]
for i in range(0,m,1):
    c=[]
    for j in range(0,m,1):
        c.append(float(input('digite o valor da linha%d e da coluna %d: ' %((j+1),(i+1)))))
    lista.append(c)

