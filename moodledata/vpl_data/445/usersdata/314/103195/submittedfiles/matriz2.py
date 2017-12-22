# -*- coding: utf-8 -*-
def lerMatrizQuadrada(matriz,t):
    for i in range(t):
        mi=[]
        for j in range(t):
            mi.append(int(input('Digite os elementos: ')))
    matriz.append(mi)  



def soma(matriz,i,j):
    sL=0
    sD=0
    for i in range(len(matriz)):
        sL = s + matriz[i][j]
        sD = sD +matriz[j][i]
        j=j+1
    return [sL,sD]
    
    


def somaDiagonal(matriz):
    somaP=0
    somaS=0
    t=len(matriz)
    for i in range (t):
        somaP=somaP + matriz[i][i]
        somaS = somaS + matriz[i][t-1-i]
    return [somaP,somaS]    



#----------------------------------------------------------------

tamanho=int(input('Digite o tamanho da matriz: '))

matriz=[]
lerMatrizQuadrada(matriz,tamanho)
soma(matriz,

print(matriz)    


    
    
    
    
    
    
    





'''tamanho=int(input('Digite o tamanho da matriz: '))

matriz=[]

for i in range(tamanho):
    mi=[]
    for j in range(tamanho):
        mi.append(int(input('Digite os elementos: ')))
    matriz.append(mi)

print(matriz)

somaC=0
somaP=0
somaS=0
magico=True
s=sum(matriz[0])


for i in range (tamanho):
    if sum(matriz[i])!=s:
        magico=False


for i in range (tamanho):
    for j in range (tamanho):
        somaC = somaC + matriz[j][i]
    if somaC!=s:
        magico=False
    somaC=0

for i in range (tamanho):
    somaP=somaP + matriz[i][i]
    somaS = somaS + matriz[i][tamanho-1-i]
if somaP!=s or somaS!=s:
    magico=False   
            

if magico==True:
    print("'S'")
else:
    print("'N'")'''
        
    
    
    