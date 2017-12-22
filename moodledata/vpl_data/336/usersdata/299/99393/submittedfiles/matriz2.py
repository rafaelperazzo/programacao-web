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
    matrizanalisecoluna=[]
    for j in range(0,len(x)-1,1):
        matriz=[]
        for i  in range(0,len(x)-1,1):
            matriz.append(x[i][j])
        matrizanalisecoluna.append(matriz)
    for i in range(0,len(matrizanalisecoluna)-1,1):
        if sum(matrizanalisecoluna[i-1])==sum(matrizanalisecoluna[i]):
            c=True
        else:
            c=False
            break
    #analise de diagonal
    matrizanalisediagonal=[]
    matrizanalisediagonal2=[]
    for i in range(0,len(x)-1,1):
        matrizanalisediagonal.append(x[i][i])
        matrizanalisediagonal2.append(x[i][len(x)-1-i])
    if sum(matrizanalise)==sum(matrizanalise2):
        c=True
    else:
        c=False
    if sum(matrizanalisecoluna[0])==sum(x[0]) and sum(x[0])==sum(matrizanalisediagonal):
        c=True
    else:
        c=False
    if c==True:
        return 'S'
    else:
        return'N'
            
matriz=[]
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)    

        
print(analisemagica(matriz))


