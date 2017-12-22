# -*- coding: utf-8 -*-
tamanho=int(input('Digite o tamanho da matriz: '))

matriz=[]

for i in range(tamanho):
    linhas=[]
    for j in range(tamanho):
        linhas.append(int(input('Digite os elementos das linhas: ')))
    matriz.append(linhas)    

print(matriz)    

soma=0
for i in range(0,len(matriz),1):
    diagonal=matriz[i][i] 
    soma=sum(matriz[i]) - diagonal
if diagonal>soma:
    print("'S'")
else:
    print("'N'")
