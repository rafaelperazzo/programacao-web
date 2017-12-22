# -*- coding: utf-8 -*-
def analisemagica(x):
    c=0
    #analise de linhas
    for i in range(1,len(x)-1,1):
        if sum(x[i-1])==sum(x[i]):
            c=True
        else:
            c=False
            break
    #analise de colunas
    matrizanalise=[]
    for j in range(0,len(x)-1,1):
        matriz=[]
        for i  in range(0,len(x)-1,1):
            matriz.append(x[i][j])
        matrizanalise.append(matriz)
    for i in range(0,len(matrizanalise)-1,1):
        if sum(matrizanalise[i-1])==sum(matrizanalise[i]):
            c=True
        else:
            c=False
  
            
matriz=[]
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)    
        
        
        
print(analisemagica(matriz))


















