# -*- coding: utf-8 -*-
l=int(input('Digite o numero de linhas da matriz: '))
c=int(input('Digite o numero de colunas da matriz: '))
m=[]
for j in range(0,l,1):
    colunas=[]
    for i in range(0,c,1):
        colunas.append(float(input('digite o elemento da linhas %d, coluna%d : ' %((j+1),(i+1)))))
    m.append(colunas)
print(m)

print(
    [9, 6, 8, 0]
    [3, 5, 4, 1]
    [2, 8, 7, 5]
    )
