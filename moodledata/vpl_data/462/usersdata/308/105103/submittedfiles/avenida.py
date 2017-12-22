# -*- coding: utf-8 -*-
def inteiro(min, max):
    valor = int(input(''))
    while not(min<=valor<=max):
        valor = int(input(''))
    return valor
matriz = []
m = inteiro(2, 1000)
n = inteiro(2, 1000)
for i in range (m):
    matriz.append([])
    for j in range (n):
        matriz[i].append(inteiro(1, 100))
        
valores = []
for j in range (n):
    total = 0
    for i in range (m):
        total += matriz[i][j]
    valores.append(total)
print(min(valores))
    
        