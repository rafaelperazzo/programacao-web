from __future__ import division
    
#DEFININDO A ENTRADA

def tom(A,n):
    contED=[]
    for i in range(0,n,1):
        cont1=0
        if A[i]==0:
            contED.append(0)
        else:
            for j in range(i,n,1):
                if A[j]==-1:
                    cont1=cont1+1
                else:
                    contED.append(cont1)
                    
    return contED

n=input('Digite a quantidade de quadrados na fita:')
A=[]

for i in range(0,n,1):
    A.append(input('Digite um valor, 0/-1: '))
    
print A
print tom(A,n)    