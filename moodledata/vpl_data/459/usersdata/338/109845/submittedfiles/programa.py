# -*- coding: utf-8 -*-
n = int(input('Digite o némro de consultas ao estoque: '))
soma = 0
matriz = []
for i in range (0,n,1):
    a = input('Digite o tamanho do taco desejado: ')
    if a in matriz:
        matriz.remove(a)
    else:
        soma += 2
        matriz.append(a)
print(soma)