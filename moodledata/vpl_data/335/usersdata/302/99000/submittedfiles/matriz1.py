# -*- coding: utf-8 -*-
def matriz01(matriz):
    m = len(matriz)
    n = len(matriz[0])
    li = m
    lf = 0
    ci = n
    cf = 0
    for i in range(li):
        for j in range(ci):
            if matriz[i][j] == 1:
                if i < li:
                    li = 1
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
    return matriz2
                
            
        
        

