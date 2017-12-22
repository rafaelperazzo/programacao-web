# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Digite a quantidade de elementos da lista: '))
lista = []
for i in range(0,n,1):
    lista.append(int(input('Digite um elemento de a: ')))
    
for i in range(0,n-1,1):
        p = 0
        h = 0
        if lista[i]<lista[i+1]:
            continue
        else:
            p = i
            break
        for t in range(p,n-1,1):
            if lista[t]>lista[t+1]:
                continue
            else:
                h = h + 1
print(p)