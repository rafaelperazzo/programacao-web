from __future__ import division
    
#DEFININDO A ENTRADA

def tom(A,n):
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
    contDE=[]
    contDE1=[]
    for i in range(n,0,-1):
        cont2=0
        for j in range(i,-2,-1):
            if A[j-1]==-1:
                cont2=cont2+1
                if j-1==0:
                    contDE.append(cont2)
                    cont2=0
            else:
                contDE.append(cont2)
                cont2=0
                break
    for y in range(n,0,-1):
        contDE1.append(contDE[y-1])
    
    resultado=[]    
    for i in range(0,n,1):
        if i==0:
            resultado.append(contED[i])
        elif i==n-1:
            resultado.append(contDE1[i])
        
        elif contDE1[i]<=contED[i]:
            resultado.append(contDE1[i])
        else:
            resultado.append(contED[i])
    
    return contED


n=input('Digite a quantidade de quadrados na fita:')
A=[]

for i in range(0,n,1):
    A.append(input('Digite um valor, 0/-1: '))
    
print tom(A,n) 
