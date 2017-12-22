# -*- coding: utf-8 -*-
matriz = []
m = int(input("Digite o número de quadras no sentido norte-sul: "))
while m<2 or m>1000:
    m = int(input("Digite o número de quadras no sentido norte-sul: "))
n = int(input("Digite o número de quadras no sentido leste-oeste: "))
while n<2 or n>1000:
    n = int(input("Digite o número de quadras no sentido leste-oeste: "))
    for i in range (0,m-1,1):
        linha = []
        for j in range (0,n-1,1):
            linha.append(int(input("Digite o valor da respectiva quadra: ")))
        matriz.append(linha)
     
                                

