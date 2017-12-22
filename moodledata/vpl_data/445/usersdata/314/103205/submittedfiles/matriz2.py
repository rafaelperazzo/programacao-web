# -*- coding: utf-8 -*
tamanho=int(input('Digite o tamanho da matriz: '))

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
    print("'N'")
        
    
    
    