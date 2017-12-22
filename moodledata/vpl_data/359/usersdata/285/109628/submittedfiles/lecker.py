# -*- coding: utf-8 -*-
n=int(input('digite o valor da lista: '))
lista_1=[]
lista_2=[]
for i in range(0,n,1):
    lista_1.append(int(input('digite o valor %d da lista 1: ' %(i+1))))
for i in range(0,n,1):
    lista_2.append(int(input('digite o valor %d da lista 2: ' %(i+1))))
#Lista 1
cont1=0
for i in range(1,n,1):
    if lista_1[i] > lista_1[i=1] and lista_1[i] > lista_1[i+1]:
        
