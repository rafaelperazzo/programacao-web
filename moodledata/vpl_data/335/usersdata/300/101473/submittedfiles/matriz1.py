# -*- coding: utf-8 -*-
def matriz(m):
    L = len(m)
    C = len(m[0])
    La = L
    Lb = 0
    Ca = C
    Cb = 0
    for i in range(L):
        for j in range(C):
            if matriz [i][j] == 1:
                if i < La:
                    La = i
                if i + 1 > Lb:
                    Lb = i + 1
                if j < Ca:
                    ci = j
                if j + 1 > Cb:
                    Cb = j + 1
    a = []
    for i in range(La,Lb):
        l = []
        for j in range(Ca,Cb):
            l.append(a[i][j])
        a.append(l)
    return print(a)
    
m = []
L = int(input('Digite o número de linhas: '))
C = int(input('Digite o número de colunas: '))
for i in range(0,L,1):
    l = []
    for j in range(0,C,1):
        l.append(int(input('Digite o elemento %d de %d: ' % ((j+1),(i+1)))))
    m.append(l)
    
matriz(m)    
    

            