# -*- coding: utf-8 -*-
tamanho=int(input('Digite o tamanho da matriz: '))

matriz=[]

for i in range(tamanho):
    mi=[]
    for j in range(tamanho):
        mi.append(int(input('Digite os elementos: ')))
    matriz.append(mi)

print(matriz)

somaL=0
somaC=0
somaD=0
magico=True
for i in range (tamanho):
    for j in range (tamanho):
        somaL = somaL + matriz[i][j]
        if somaL!=magico:
            magico=False


for i in range (tamanho):
    for j in range (tamanho):
        somaC = somaC + matriz[j][i]
        if somaC!=magico:
            magico=False

for i in range (tamanho):
   somaD = somaD + matriz[i][tamanho-i]
        if somaD!=magico:
            magico=False    
            
if magico==True:
    print("'S'")
else
    print("'N'")
        
    
    
    