# -*- coding: utf-8 -*-















lista1=[]
lista2=[]

n1=int(input('digite o numero de elementos da lista1: '))
n2=int(input('digite o numero de elementos da lista2: '))

for i in range(0,len(lista1)-1,1):
    lista1.append(int(input('digite um valor%.d: ' %(i+1))))
print(lista1)
