# -*- coding: utf-8 -*-
def matriz01(matriz):
    m = len(matriz)
    n = len(matriz[0])
    la = m
    lb = 0
    ca = n
    cb = 0
    for i in range(m):
        for j in range(n):
            if matriz[i][j] == 1:
                if i < la:
                    la = i
                if i + 1 > lb:
                    lb = i + 1
                if j < ca:
                    ca = j
                if j + 1 > cb:
                    cb = j + 1
    matriz2 = []
    for i in range(la,lb):
        l = []
        for j in range(ca,cb):
            l.append(matriz[i][j])
        matriz2.append(l)
    return print(matriz2)
    
matriz = []
m = int(input('Digite o número de linhas: '))
n = int(input('Digite o número de colunas: '))
for i in range(0,m,1):
    l = []
    for j in range(0,n,1):
        l.append(int(input('Digite o elemento %d de %d: ' % ((j+1),(i+1)))))
    matriz.append(l)
    
matriz01(matriz)    
    

            