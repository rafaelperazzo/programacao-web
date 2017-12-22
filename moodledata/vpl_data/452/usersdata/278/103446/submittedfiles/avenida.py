# -*- coding: utf-8 -*-
m = int(input('Digite o número de quadras no sentido Norte-Sul: '))
n = int(input('digite o número de quadras no sentido Leste-Oeste: '))
valor = []
for i in range (0,m,1):
    for j in range (0,n,1):
        valor.append(int(input('Digite o valor de desapropriação da quadra%d%d: ' %(i+1,j+1))))
        