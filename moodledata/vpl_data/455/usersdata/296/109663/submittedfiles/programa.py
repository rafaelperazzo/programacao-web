# -*- coding: utf-8 -*-
#CIRANDO O QUADRADO
n = int(input("Digite a dimensão do quadrado: "))
while not n>=3:
    n = int(input("Digite a dimensão do quadrado: "))
matriz =[]
for i in range (0,n,1):
    linha = []
    for j in range (0,n,1):
        linha.append(int(input("Digite um valor para o elemento da linha: "))
    matriz.append(linha)
#VERIFICANDO SE É UM QUADRADO_MÁGICO
