# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

    #FUNÇÃO PARA TESTAR SE UMA MATRIZ É UM QUADRADO MÁGICO!

def qMagico(m):

    #PRIMEIRO ENCONTRAR A SOMA DE CADA LINHA E COMPARÁ-LAS...

    cont1=0
    
    for i in range (0,m.shape[0]-1,1):
        if sum(m[i,:])==sum(m[i+1,:]):
            cont1=cont1+1

    #DEPOIS COMPARAR O NÚMERO DE IGUALDADES A QUANTIDADE DE LINHAS -1

    if cont1==m.shape[0]-1: 
        somaLinhas=sum(m[0,:])
    else:
        somaLinhas=0
    #AQUI FOI ATRIBUIDO UM VALOR QUALQUER A SOMA DAS 
    #LINHAS NO CASO DE ELAS NÃO TEREM OS MESMOS VALORES DE SOMA



    #AGORA FAZER O MESMO COM AS COLUNAS...

    cont2=0
    
    for j in range (0,m.shape[1]-1,1):
        if sum(m[:,j])==sum(m[:,j]):
            cont2=cont2+1
    
    if cont2==m.shape[0]-1:
        somaColunas=sum(m[:,0])
    else:
        somaColunas=1
    #NO CASO DE AS COLUNAS NÃO TEREM AS SUAS SOMAS IGUAIS,
    #É ATRIBUIDO UM VALOR PARA SOMA, DIFERENTE DO VALOR DA SOMA DAS LINHAS



    #PARA A DIAGONAL PRINCIPAL FORAM SOMADOS APENAS OS VALORES
    #COM COORDENADAS IGUAIS (MELHOR PARTE)

    somaD1=0
    for k in range(0,m.shape[0],1):
        somaD1=somaD1+m[k,k]

    somaDiagonal1=somaD1
        

    #E PARA A OUTRA DIAGONAL, O VALOR DA COORDENADA DA LINHA COMEÇOU EM ZERO
    #E FOI AUMENTANDO DE UM EM UM. AO PASSO EM QUE AS COORDENADAS DE COLUNA FORAM
    #DIMINUINDO DE UM EM UM
    cont4=0
    somaD2=0
    j=m.shape[1]-1
    i=0
    
    while cont4 < m.shape[0]:
        somaD2=somaD2+m[i,j]
        cont4=cont4+1
        
        j=j-1
        i=i+1
        
    somaDiagonal2=somaD2
            
    #POR ÚLTIMO COMPARA-SE OS QUATRO VALORES...

    if somaLinhas==somaColunas==somaDiagonal1==somaDiagonal2:
        return True
    else:
        return False





#COMO É UMA MATRIZ QUADRADA, SÓ PRECISA SER INFORMADA A DIMENSÃO

n=input('Dimensão da matriz: ')
m=np.zeros((n,n))

for i in range (0,m.shape[0],1):
    for j in range (0,m.shape[1],1):
        m[i,j]=input('Digite um termo: ')

if qMagico(m):
    print 'S'
else:
    print 'N'
