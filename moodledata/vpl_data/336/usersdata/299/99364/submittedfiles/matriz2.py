# -*- coding: utf-8 -*-
def analisemagica(x):
    c=0
    #analise de linhas
    for i in range(1,len(x),1):
        if sum(x[i-1])==sum(x[i]):
            c=True
        else:
            c=False
            break
    #analise de colunas
    for j in range(0,len(x)-1,1):
        matrizanalise=[]
        for i  in range(0,len(x)-1,1):
            matrlizanalise.append(x[i][j])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
matriz=[]
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)    
        
        
        
print(analisemagica(matriz))


















