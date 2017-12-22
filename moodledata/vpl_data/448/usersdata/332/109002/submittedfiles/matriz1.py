# -*- coding: utf-8 -*-
a=int(input('digite o numero de linhas da matriz:'))
b=int(input('digite o numero de colunas da matriz:'))
m=[]
for j in range(0,a,1):
    colunas=[]
    for i in range(0,a,1):
        colunas.append(float(input('digite o elemento da linha %d, coluna%d : %((j+1),(i+1)))))
        m.append(colunas)
        print(m)

