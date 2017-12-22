# -*- coding: utf-8 -*-
def analisemagica(x):
    c=0
    #analisando a soma  linha 0 com a soma coluna 0 e com a soma diagonal principal
    #criando vetor diagonal principal
    vetordiagonalp=[]
    for i in range(0,len(x)-1,1):
        vetordiagonalp.append(x[i][i])
    #criando vetor coluna 0
    vetorcoluna0=[]
    for i in range(0,len(x)-1,1):
        vetorcoluna0.append(x[i][0])
    #comparação das somas
    if sum(vetordiagonalp)==sum(vetorcoluna0) and sum(vetorcoluna0)==sum(x[0]):
        c=True
        #analisar soma de linha
        for i in range(1,len(x)-1,1):
            if sum(x[i-1])==sum(x[i]):
                c=True
            else:
                return 'N'
                break
        #se a as somas nas linhas forem iguais
        if c==True:
            #analisar soma de coluna
            #criando uma matriz com linhas iguais as colunas de x
            matrizcoluna=[]
            for j in range(0,len(x)-1,1):
                matriz=[]
                for i in range(0,len(x)-1,1):
                    matriz.append(x[i][j])
                matrizcoluna.append(matriz)
            #comparando as linhas da matrizcoluna
            for i in range(1,len(x)-1,1):
                if sum(matrizcoluna[i-1])==sum(matrizcoluna[i]):
                    c=True
                else:
                    return 'N'
                    break
            #se as somas nas linhas da matrizcoluna forem iguais
            if c==True:
                #analisar segunda diagonal
                vetordiagona2=[]
                for i in range(0,len(x),1):
                    vetordiagonal2.append(x[i][len(x)-1-i])
                if sum(vetordiagonal2)==sum(vetordiagonalp):
                    c=True
                #se a igualdade das diagonais não acontecer
                elif sum(vetordiagonal2)!=sum(vetordiagonalp):
                    return 'N'
            #se a igualdade das colunas não acontecer 
            elif c!=True:
                return 'N'
        #se a igualdade das linhas não acontecer
        elif c!=True:
            return 'N'
    #se a igualdade da soma da linha0,coluna0 e da diagonal principal não acontecer
    elif sum(vetordiagonalp)!=sum(vetorcoluna0) or sum(vetorcoluna0)!=sum(x[0]):
        return 'N'
    

    

matriz=[]
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)    

        
print(analisemagica(matriz))


