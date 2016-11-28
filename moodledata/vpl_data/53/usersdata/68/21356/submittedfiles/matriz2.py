# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#DIAGONAL PRINCIPAL
def somaDiagonal1(a):
    soma=0
    for i in range (0, a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
#DIAGONAL SECUNDÁRIA
def somaDiagonal2(a):
    soma=0
    i=0
    j=a.shape[0]-1
    while j>=0:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma 
    
#SOMA DAS LINHAS (PIOR PARTE)
def somaLinhas(a):
    l=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        l.append (soma)
    return l

#SOMA DAS COLUNAS (PIOR PARTE 2)
def somaColunas(a):
    c=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
        c.append (soma)
    return c

#QUADRADO MÁGICO, SIM OU NÃO? EIS A QUESTÃO
def quadradoMagico(a):
    sdp=somaDiagonal1(a)
    sds=somaDiagonal2(a)
    sl=somaLinhas(a)
    sc=somaColunas(a)
    cont=0
    for i in range (0, len(sl),1):
        if sdp==sds==sl[i]==sc[i]:
            cont=cont+1
    if cont==len(sl): #<-------------------- O ERRO ESTAVA AQUI!! ESTE IF DEVE SER FEITO APÓS A REPETIÇÃO E NÃO DENTRO DA REPETIÇÃO!
        return True
    else:
        return False
        
#PROGRAMA PRINCIPAL 
n=input('Digite o tamanho da matriz:')
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento da matriz a:')

if quadradoMagico (a):
    print ('S')
else:
    print ('N')
    