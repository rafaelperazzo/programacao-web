# -*- coding: utf-8 -*-
matriz=[]
m=int(input('Digite a ordem da matriz:'))
while m<2 or m>1000:
    m=int(input('Digite a ordem da matriz:'))
for i in range(0,m,1):
    linha=[]
    n=int(input('Digite a 2ordem da matriz:'))
    for j in range(0,n,1):
        linha.append(int(input('Digite a linha/coluna:')))
    matriz.append(linha)

linhaS=[]
for i in range(0,m,1):
    sl=0
    for j in range(0,m,1):
        sl+=matriz[i][j]
    linhaS.append(sl)
print(linhaS)
colunaS=[]
for j in range(0,m,1):
    sc=0
    for i in range(0,m,1):
        sc+=matriz[i][j]
    colunaS.append(sc)
print(colunaS)

if min(linhaS)<min(colunaS):
    print(min(linhaS))
else:
    min(colunaS)






        