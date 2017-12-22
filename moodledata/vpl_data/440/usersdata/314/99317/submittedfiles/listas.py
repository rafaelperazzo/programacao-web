# -*- coding: utf-8 -*-
import math


n = int(input())

lista = [ ]

#leitura da lista de numeros
for i in range(0, n, 1):
    lista.append(int(input()))
    
    
diferenca = [ ]

for i in range(0, len(lista)-1, 1):
    diferenca.append(math.fabs(lista[i] - lista[i + 1]))
    
maior = diferenca[0]
for i in range(1, len(lista)-1, 1):
    if diferenca[i] > maior:
        maior = diferenca[i]
    
print(math.fabs(maior))      

    
