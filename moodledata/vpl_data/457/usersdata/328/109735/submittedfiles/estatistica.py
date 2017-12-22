# -*- coding: utf-8 -*-
while True:
    n=int(input('Digite o número de elementos da lista:'))
    if n>=2:
        break
#matriz principal
matriz=[]
for i in range(n):
    linhas=[]
    for j in range(n):
        linhas.append(int(input('Insira elementos:')))
    matriz.append(linhas)
#matriz transposta
mt=[]
for i in range(n):
    ve=[]
    for j in range(n):
        ve.append(matriz[j][i])
    mt.append(ve)
som=0
for i in range (n):
    for j in range (n): 
        if (sum(matriz[i])-matriz[i][j])+(sum(mt[j])-matriz[i][j])>som:
            som=(sum(matriz[i])-matriz[i][j])+(sum(mt[j])-matriz[i][j])
    print(som)
