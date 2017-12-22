# -*- coding: utf-8 -*-
matriz = []
m = int(input("Digite o número de quadras no sentido norte-sul: "))
while 2<=m<=1000:
    m = int(input("Digite o número de quadras no sentido norte-sul: "))
n = int(input("Digite o número de quadras no sentido leste-oeste: "))
while 2<=m<=1000:
    n = int(input("Digite o número de quadras no sentido leste-oeste: "))
for i in range (0,m,1):
    linha = []
    for j in range (0,n,1):
        linha.append(int(input("Digite o valor da respectiva quadra: ")))
    matriz.append(linha)
