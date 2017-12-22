# -*- coding: utf-8 -*-
lista=[]
n=int(input('digite a quantidade de elementos: '))
for i in range (0,n,1):
    lista.append(float(input('digite o valor do elemento%d:' % (i+1))))
for i in range (0,n,1):
    if [lista[i]]%2 != 0:
        print(sum(lista[i]))



