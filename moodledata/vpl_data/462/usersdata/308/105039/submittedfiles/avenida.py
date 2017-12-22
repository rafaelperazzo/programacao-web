# -*- coding: utf-8 -*-
def inteiro(texto, min, max):
    valor = int(input(texto))
    while not(min<=valor<=max):
        valor = int(input(texto))
    return valor
matriz = []
m = inteiro('Informe a quantidade de quadras no sentido Norte-Sul: ', 2, 1000)
n = inteiro('Informe a quantidade de quadras no sentido Leste-Oeste: ', 2, 1000)
for i in range (m):
    matriz.append([])
    for j in range (n):
        matriz[i].append(inteiro('Informe o valor da quadra %d %d: ' % (i+1, j+1), 1, 100))
print(M)