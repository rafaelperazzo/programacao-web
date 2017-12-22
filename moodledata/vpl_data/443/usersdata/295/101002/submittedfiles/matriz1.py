# -*- coding: utf-8 -*-
matriz = []
m = int(input("Digite o numero de linhas da matriz :"))
n = int(input("Digite o numero de colunas da matriz :"))
for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        linha.append(int(input("Digite o valor do %dº elemento da %dª lista : " %((j+1),(i+1)))))
    matriz.append(linha)

def rodar(matriz, grau):
    nova_matriz = copy.deepcopy(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if grau == 180:
                nova_matriz[len(matriz)-(i+1)][len(matriz)-(j+1)] = matriz[i][j]
    return nova_matriz
    
if _name_ == "_mian_":
    print(rodar)
    
