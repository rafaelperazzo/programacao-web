# -*- coding: utf-8 -*-
def analisemagica(x):
    colunas=[]
    c=0
    l=0
    d=0
    for j in range(0,len(x)-1,1):
        linha=[]
        for i in range(0,len(x)-1,1):
            linha.append(x[i][j])
        colunas.append(linha)
    # comparando as colunas
    for i in range(1,len(colunas)-1,1):
        if sum(colunas[i-1])==sum(colunas[i]):
            c=True
        else:
            return 'N'
        
    linhas=[]
    for i in range(0,len(x)-1,1):
        linhas.append(x[i])
    #comparando as linhas
    for i in range(1,len(linhas)-1,1):
        if sum(linhas[i-1])==sum(linhas[i]):
            l=True
        else:
            return 'N'
        
    diagonalp=[]
    for i in range(0,len(x)-1,1):
        diagonalp.append(x[i][i])
    diagonal2=[]
    for i in range(0,len(x)-1,1):
        diagonal2.append(x[i][len(x)-2-i])
    if sum(diagonalp)==sum(diagonal2):
        d=True
    else:
        return 'N'
    if c==d and d==l:
        return 'S'
    else:
        return 'N'

matriz=[]
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)    

        
print(analisemagica(matriz))


