# -*- coding: utf-8 -*-
import numpy as np
dimensao= int(input('Digite a dimensao: '))
x=int(input('Digite a linha'))
y= int(input('Digite a coluna'))
a=np.zeros((dimensao.dimensao))

 for i in range(0,a.shape[0],1):
     for j in range(0,a.sape[1],1):
         a[i,j]= int(input('Digite o elemeto: '))
         
def soma_linha(matriz,linha):
    soma=0
    for j in range(0,matriz.shape[1],1):
        soma=soma +matriz[linha,j]
        return(soma)
def soma_coluna(matriz,coluna):
    soma=0
    for i in range (0,matriz.shape[0],1):
        soma=soma+matriz[i,coluna]
        return(soma)
        
final= soma_linha(a,x) + soma_coluna(a,y) - (2*a[x,y])
print(int(final))

