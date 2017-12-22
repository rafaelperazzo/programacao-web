# -*- coding: utf-8 -*-
n=0
while n<3:
    n=int(input('digite o numero de linhs/colunas que tera o quadrado: '))
matriz=[]
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input('digite o elemento da linha%d e coluna%d: '%((i+1),(j+1)))))
    matriz.append(linha)
cont=0
cont2=0
soma=0
soma2=0
soma_anterior2=0
soma_anterior=sum(matriz[0])
for i in range(n):
    soma=sum(matriz)
    if soma_anterior==soma:
        cont+=1
        ai=ai+1
    elif cont==0:
        errada=matriz[0]
        bi=bi+1
    else:
        errada=matriz[i]
        ci=ci+1
for j in range(0,1,1):
    for i in range(n):
        soma_anterior2+=matriz[i][j]
for j in range(n):
    for i in range(n):
        soma2+=matriz[i][j]
    if soma2==soma_anterior2:
        cont2+=1
        di=di+1
    elif cont2==0:
        errada2=matriz[i][0]
        ei=ei+1
    else:
        errada2=matriz[i][j]
        fi=fi+1
if ci==fi:
elif bi==ei:

    
    
    