# -*- coding: utf-8 -*-
def analisemagica(x):
    c=0
    #analise soma  linha 0 soma coluna 0 e soma diagonal principal
    vetordiagonalp=[]
    for i in range(0,len(x)-1,1):
        vetordiagonalp.append(x[i][i])
    vetorcoluna0=[]
    for i in range(0,len(x)-1,1):
        vetorcoluna0.append(x[i][0])
    if sum(vetordiagonalp)==sum(vetorcoluna0) and sum(vetordiagonalp)==sum(x[0]):
        c=True
        #analisar soma de linha
        for i in range(1,len(x)-1,1):
            if sum(x[i-1])==sum(x[i]):
                c=True
            else:
                c=False
                break
        if c==True:
            #analisar soma de coluna
            matrizcoluna=[]
            for j in range(0,len(x)-1,1):
                matriz=[]
                for i in range(0,len(x)-1,1):
                    matriz.append(x[i][j])
                matrizcoluna.append(matriz)
            for i in range(1,len(matrizcoluna)-1,1):
                if sum(matrizcoluna[i-1])==sum(matrizcoluna[i]):
                    c=True
                else:
                    c=False
                    break
            if c==True:
                #analisar segunda diagonal
                vetordiagona2=[]
                for i in range(0,len(x),1):
                    vetordiagonal2.append(x[i][len(x)-1-i])
                if sum(vetordiagonal2)==sum(vetordiagonalp):
                    c==True
                else:
                    c==False
            else:
                c==False
        else:
            c==False
    else:
        c=False
    
    if c==True:
        return 'S'
    else:
        return 'N'
    
    
    
    
    
    
    
    
    
    
    
    
    
            
matriz=[]
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)    

        
print(analisemagica(matriz))


