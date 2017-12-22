# -*- coding: utf-8 -*-
n=int(input('digite o número de seções que a piscina tem: '))
lista=[]
for i in range(0,n,1):
    lista.append(int(input('digite a o elemento altura da seção%d: '%(i+1))))
    