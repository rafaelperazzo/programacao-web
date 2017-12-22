# -*- coding: utf-8 -*-


n=0
while n<3:
    n=int(input('Digite a dimensão da matriz: '))


#TENTAR FAZER FUNÇÃO "DIFERENTE" PARA ACHAR A LINHA E A COLUNA CUJA SOMA SEJA DIFERENTE DAS DEMAIS
def soma:
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
            





for i in range(0,n,1):
    soma=0
    for j in range(0,n,1):
        soma=soma+a[i,j]
    somaL=soma
    soma=0
    for j in range(0,n,1):
        soma=soma+a[j,i]
    coluna.append(soma)
    
    
    
    
a=0
b=1
c=2
while linha[a]=linha[b]:
    
#for i in range(1,len(linha),1):
    if linha[a]=linha[b]:
        diferente=i+1
        