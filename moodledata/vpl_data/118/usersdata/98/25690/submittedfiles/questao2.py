from __future__ import division
    
#DEFININDO A ENTRADA

def tom1(A,n):
    contED=[]
    for i in range(0,n,1):
        cont1=0
        for j in range(i,n,1):
            if A[j]==-1:
                cont1=cont1+1
                if j==n-1:
                    contED.append(cont1)
                    
            else:
                contED.append(cont1)
                cont1=0
                break
    return contED
    

def tom2(A,n):
    contDE=[]
    contDE1=[]
    for i in range(n,0,-1):
        cont2=0
        for j in range(i,-2,-1):
            if A[j-1]==-1:
                cont2=cont2+1
                if A[j-1]==0:
                    contDE.append(cont2)
                    oont2=0
            else:
                contDE.append(cont2)
                cont2=0
                break
    for y in range(n,0,-1):
        contDE1.append(contDE[y-1])
        
    return contDE
    
n=input('Digite a quantidade de quadrados na fita:')
A=[]

for i in range(0,n,1):
    A.append(input('Digite um valor, 0/-1: '))
    
print A
print tom1(A,n) 
print tom2(A,n)