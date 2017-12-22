# -*- coding: utf-8 -*-
matriz=[]
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)
cont=0
for i in range(0,n,1):
    if int(matriz[i][i])>(sum(matriz[i])-int(matriz[i][i])):
        cont+=0
    else:
        cont+=1
        
if cont==0:
    print('SIM')
else:
    print('NAO')
            
        