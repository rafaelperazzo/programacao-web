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
s=sum(matriz[0])
for i in range (tamanho):
    somaL = somaL + sum(matriz[i])
    if somaL!=s:
        magico=False

print(somaL)
'''for i in range (tamanho):
    for j in range (tamanho):
        somaC = somaC + matriz[j][i]
        if somaC!=s:
            magico=False

for i in range (tamanho):
    somaD = somaD + matriz[i][tamanho-1-i]
    if somaD!=s:
        magico=False '''   
            

if magico==True:
    print("'S'")
else:
    print("'N'")
        
    
    
    