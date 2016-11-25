# -*- coding: utf-8 -*-
from __future__ import division
#1passo:calcular o somatório das diagonáis principais
def somaDiagonal1(a):
    soma=0
    for i in range(0, a.shape[0],1):
        soma=soma+a[i,i]
    return soma
#2passo:calcular o somatório da diagonal secundária
def somaDiagonal2(a):
    soma=0
    for i in range(0, a.shape[0],1):
        soma=soma+a[i,a.shape[0]-i-1]
    return soma    

#3passo:calcular os somatórios das colunas e das linhas
#soma das linhas
def somaLinhas(a):
    s=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s
    
#soma das colunas
def somaColuna(a):
    s=[]
    for j in range(0,a.shape[0],1):
        soma=0
        for i in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s    
    
#entrada da matriz
def quadroMagico(a):
    
    sd1=somaDiagonal1(a)
    sd2=somaDiagonal2(a)
    
    somaL=somaLinhas(a)
    somaC=somaColunas(a)
    
    cont=0
    for i in range(0,len(somaL),1):
        if sd1==sd2==somaL[i]==somaC[i]:
            cont=cont+1
            
    if cont==len(somaL):
        return True
    else:
        return False
        
#programa principal
n=input('digite a dimensão da matriz:')
a=np.zeros((n,n))
for i in range(0,a.shape[],1):
    for j in range(0, a.shape[],1):
        a[i,j]=input()
        
if quadradoMagico(a):
    print('S')
else:
    print('N')
