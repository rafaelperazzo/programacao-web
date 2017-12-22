# -*- coding: utf-8 -*-
matriz=[]
m=int(input('Digite a ordem da matriz:'))
for i in range(0,m,1):
    n=[]
    for j in range(0,m,1):
        n.append(int(input('Digite a linha/coluna:')))
    matriz.append(n)

linhaS=[]
for i in range(0,m,1):
    sl=0
    for j in range(0,m,1):
        sl+=matriz[i][j]
    linhaS.append(sl)
colunaS=[]
for j in range(0,m,1):
    sc=0
    for i in range(0,m,1):
        sc+=matriz[i][j]
    linhaS.append(sc)

menor=0
for i in range(0,m,1):
    if menor> linhaS[0]:
        menor=linhaS[0]
print(linhaS)
print(menor)




        