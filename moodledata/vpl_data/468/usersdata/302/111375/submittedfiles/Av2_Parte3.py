# -*- coding: utf-8 -*-
def q_listas(m,lista,n):
    m = int(input('Digite a quantidade de listas: '))
    n = int(input('Digite o número de elementos das listas: '))
    i = 0
    while(i <= m):
        lista = []
        for j in range(n):
            lista.append(float(input('Digite o elemento %d da lista %d' %((j+1),(i+1)))))
        i += 1
m = int(input('Digite a quantidade de listas: '))
n = int(input('Digite o número de elementos das listas: '))
a = []
q_lista(m,a,n)
