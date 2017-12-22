# -*- coding: utf-8 -*-#
M=int(input("Digite o valor de M: "))
N=int(input("Digite o valor de N: "))
quadra=[]

for i in range(0,M,1):
    quadra_linha=[]
    for j in range(0,N,1):
        quadra_linha.append(int(input("Digite o valor (%d,%d): "%(M+1,N+1))))
    quadra.append(quadra_linha)
print(quadra)