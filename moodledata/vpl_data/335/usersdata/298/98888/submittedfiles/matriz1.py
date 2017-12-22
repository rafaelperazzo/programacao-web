# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de linhas da matriz: '))
m = int(input('Digite a quantidade de colunas da matriz: '))

matriz=[]
for l in range (0, n, 1):
    linha=[]
    for i in range (0, m, 1):
        linha.append(int(input('Digite um elemento para a matriz: ')))
    matriz.append(linha)


def verifica_linha_nula (matriz):
    listanulas=[]
    for i in range (0, len(matriz), 1):
        cont=0
        for j in range (0, len(matriz[i]), 1):
            if matriz[i][j]==0:
                cont+=0
            if not matriz[i][j]==0:
                cont+=1
        if cont==0:
            listanulas.append(True)
        if not cont==0:
            listanulas.append(False)
    return listanulas
    
def verifica_coluna_nula (matriz):
    colnul=[]
    for i in range (0, len(matriz), 1):
        cont=0
        for r in range (0, len(matriz[i], 1):
            if matriz[r][i]==0:
                cont+=0
            if not matriz[j][i]==0:
                cont+=1
        if cont==0:
                colnul.append(True)
        if not cont==0:
                colnul.append(False)
    return colnul
    
k = verifica_linha_nula (matriz)
for i in range (0, len(k), 1):
    if k[i]==True:
        del matriz[i]

g = verifica_coluna_nula (matriz)
for j in range (0, len(g), 1):
    if g[j]==True:
        for u in range (0, len(matriz), 1):
            del matriz[u][j]

print(matriz)













