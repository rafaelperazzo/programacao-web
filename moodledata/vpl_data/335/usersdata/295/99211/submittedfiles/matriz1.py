# -*- coding: utf-8 -*-
def matriz01(matriz):
    m = len(matriz)
    n = len(matriz[0])
    li = m
    lf = 0
    ci = n
    cf = 0
    for i in range(m):
        for j in range(n):
            if matriz[i][j] == 1:
                if i < li:
                    li = i
                if i + 1 > lf:
                    lf = i + 1
                if j < ci:
                    ci = j
                    if j+1 > cf:
                        cf = j+1
    matriz2 = []
    for i in range(li,lf):
        linha = []
        for j in range(ci,cf):
            linha.append(matriz[i][j])
        matriz2.append(linha)
    return print(matriz2)
    
    
matriz = []
m = int(input("Digite a qtd de linhas: "))
n = int(input("Digite a qtd de colunas: "))
for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        linha.append(int(input("Digite o elemento %d de %d: " %((j+1),(i+1)))))
    matriz.append
        
matriz01(matriz)
        

    
    
