from __future__ import division
    
#DEFININDO A ENTRADA

def tom1(A,n):
    contED=[]
    for i in range(0,n,1):
        cont1=0
        for j in range(i,n,1):
            if A[j]==-1:
                cont1=cont1+1
            else:
                contED.append(cont1)
                cont1=0
                break
    return contED
    
def tom2(A,n):
    contDE=[]
    cont2=0
    for i in range(n-1,0,1):
        
        for j in range(i,0,-1):
            if A[j]==-1:
                cont2=cont2+1
            else:
                contDE.append(cont2)
                cont1=0
                break
    return contDE
    
n=input('Digite a quantidade de quadrados na fita:')
A=[]

for i in range(0,n,1):
    A.append(input('Digite um valor, 0/-1: '))
    
print A
print tom1(A,n) 
print tom2(A,n)