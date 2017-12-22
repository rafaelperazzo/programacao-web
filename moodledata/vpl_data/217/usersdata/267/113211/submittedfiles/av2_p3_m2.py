# -*- coding: utf-8 -*-
import numpy as np

#FUNÇÃO
def Ldiferente(a,valorsoma):
    for i in range(0,n,1):
        soma=0
        for j in range(0,n,1):
            soma=soma+a[i,j]
        if valorsoma!=soma:
            return(i)
        
def Cdiferente(a,valorsoma):
    for j in range(0,n,1):
        soma=0
        for i in range(0,n,1):
            soma=soma+a[i,j]
        if valorsoma!=soma:
            return(j)
    
def valorsoma(a):
    A=0
    B=0
    C=0
    for i in range(0,n-2,1):
        for j in range(0,n,1):
            A=A+a[i,j]
            B=B+a[i+1,j]
            C=C+a[i+2,j]
        if A==B:
            return(A)
        if A==C:
            return(A)
        if B==C:
            return(B)
            
#PROGRAMA PRINCIPAL 
n=0
while n<3:
    n=int(input('Digite a dimensão da matriz: '))
matriz=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        matriz[i,j]=int(input('Digite o valor da posição %d%d: '%(i+1,j+1)))
valor=valorsoma(matriz)
linha=Ldiferente(matriz,valor)
coluna=Cdiferente(matriz,valor)
soma=0
for i in range(0,n,1):
    soma=soma+matriz[linha,i]
erro=soma-matriz[linha,coluna]
original=valor-erro
print('soma linha: %d' %soma)
print('soma correta: %d' %valor)
print(original)
print(erro)
