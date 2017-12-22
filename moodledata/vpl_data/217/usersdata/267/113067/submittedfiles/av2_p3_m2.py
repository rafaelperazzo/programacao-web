# -*- coding: utf-8 -*-

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
        if A=B:
            return(A)
        if A=C:
            return(A)
        if B=C:
            return(B)
            
#PROGRAMA PRINCIPAL 
n=0
while n<3:
    n=int(input('Digite a dimensão da matriz: '))

valor=valorsoma(matriz)
    
    

a=0
b=1
c=2

        