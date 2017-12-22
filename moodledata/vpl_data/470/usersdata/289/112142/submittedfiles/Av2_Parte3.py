# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de listas: "))
n=int(input("Digite a quantidade de elementos de cada lista:"))
for i in range(0,m,1):
    l=[]
    for j in range(0,n,1):
        l.append(int(input("Digite o elemento%.d da lista%.d:" %(i+1,j))))
