# -*- coding: utf-8 -*-
import statistics

m=int(input('Digite a quantidade de listas: '))
n=int(input('Digite a quantidade de elementos das listas: '))
a=[]
for i in range(0,m,1):
    for i in range(0,n,1):
        valor=float(input('Digite o elemento da lista: ')
        a.append(valor)
    print('%.2f' %statistics.mean(a))
    print('%.2f' %statistics.pstdev(a))