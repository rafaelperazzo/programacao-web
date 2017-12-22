# -*- coding: utf-8 -*-
n = int(input('tamanho: ' ))
lista = []
for i in range (n):
    lista.append(int(inpu('informe os elementos: ')))
    
limpar = []
lpar = []
for i in range (n):
    if lista[i]%2 == 0:
        lpar.append(lista[i])
    else:
        limpar.append(lista[i])
        
print(sum(limpar))
print(sum(lpar))
print(len(limpar))
print(len(lpar))
print(lista)