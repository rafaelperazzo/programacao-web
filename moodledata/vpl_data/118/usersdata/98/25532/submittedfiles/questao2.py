from __future__ import division
import numpy as np

#CRIANDO A FUNÇÃO

    #Da Esquerda para Direita:
def tom(A,n):
    L=[]
    contED=[]

    for i in range(0,n,1):
        if A[i]==0:
            L[i]=0
            contED.append(0)
        else:
            for j in range(0,n,1):
                cont1=0
                if A[j]==-1:
                    cont1=cont1+1
                else:
                    contED.append(cont1)
                    break
    return contED
    #Da Direita para Esquerda:
def tom(A,n):
    L=[]
    contED=[]

    for i in range(0,n,1):
        if A[i]==0:
            L[i]=0
            contED.append(0)
        else:
            for j in range(0,n,1):
                cont1=0
                if A[j]==-1:
                    cont1=cont1+1
                else:
                    contED.append(cont1)
                    break
                
                
            
        

#DEFININDO A ENTRADA

n=input('Digite a quantidade de quadrados na fita:')
A=[]

for i in range(0,n,1):
    A.append(input('Digite um valor, 0/-1: '))
    
print tom(A,n)
    