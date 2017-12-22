# -*- coding: utf-8 -*-
while True:
    tabuleiro=int(input('Digite o tamanho tabuleiro: '))
    if tabuleiro>=3:
        break
    

matriz=[]
for i in range(tabuleiro):
    linhas=[]
    for j in range(tabuleiro):
        linhas.append(int(input('Digite os elementos do tabuleiro: ')))
    matriz.append(linhas)
    

pesomaximo = 0
soma = 0

for i in range(0,len(matriz),1):
    for j in range(0,len(matriz),1):
        soma+= sum(matriz[i]) - 2*matriz[i][j]
        for l in range(0,len(matriz),1):
            soma+=matriz[l][j]
        if soma>pesomaximo:
            pesomaximo=soma
        soma=0


print(pesomaximo)        
            