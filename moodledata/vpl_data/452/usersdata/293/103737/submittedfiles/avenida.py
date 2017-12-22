# -*- coding: utf-8 -*-#
M=int(input("Digite o valor de M: "))
while(True):
    if M<2 or M>1000:
        M=int(input("Digite o valor de M: "))
    else:
        break
    
N=int(input("Digite o valor de N: "))
while(True):
    if N<2 or N>1000:
        N=int(input("Digite o valor de N: "))
    else:
        break

quadra=[]

for i in range(0,M,1):
    quadra_linha=[]
    for j in range(0,N,1):
        elemento=float(input("Digite o valor (%d,%d): "%(i+1,j+1)))
        while(True):
            if elemento<1 or elemento>100:
                    elemento=float(input("Digite o valor (%d,%d): "%(i+1,j+1)))
            else:
                break
        quadra_linha.append(elemento)
    quadra.append(quadra_linha)
soma_colunas=[]
for j in range(0,N,1):
    quadra_coluna=0
    for i in range(0,M,1):
        quadra_coluna= quadra_coluna + quadra[i][j]
    soma_colunas.append(quadra_coluna)
print(soma_colunas)
        

