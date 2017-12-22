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
soma_linha=0
soma_col=0
for i in range(1,2,1):
    if sum(matriz[i])==sum(matriz[i-1]):
        soma_linha=sum(matriz[i])
    elif sum(matriz[i])==sum(matriz[i+1]):
        soma_linha=sum(matriz[i])
    elif sum(matriz[i-1])==sum(matriz[i+1]) :
        soma_linha=sum(matriz[i+1])
for j in range(0,3,1):
    list_sum_col=[]
    soma_coluna=0
    for i in range(0,n,1):
        soma_coluna+=matriz[i][j]
    list_sum_col.append(soma_coluna)
if list_sum_col[0]==list_sum_col[1]:
    soma_col=list_sum_col[0]
elif list_sum_col[0]==list_sum_col[2]:
    soma_col=list_sum_col[0]
elif list_sum_col[1]==list_sum_col[2]:
    soma_col=list_sum_col[1]
print(soma_col)
'''for i in range(0,n,1):
    if sum(matriz[i])!=soma_linha:
        erro_linha=matriz[i]
for j in range(0,n,1):
    for i in range(0,n,1):
        sum_col+=matriz[i][j]
    if soma_col!=sum_col:
        erro_col=sum_col
        break'''
