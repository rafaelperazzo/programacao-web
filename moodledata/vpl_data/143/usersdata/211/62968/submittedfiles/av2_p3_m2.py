# -*- coding: utf-8 -*-
def degrau(A,B)
    for i in range(0,n-1,1):
        Soma=(A[i]-A[i+1])
        if Soma<0:
            Soma=Soma*(-1)
        if Soma>Degrau:
            Degrau=Soma
    return Degrau
H=int(input('escreva o valor de H:'))
K=[]
for i in range(0,H,1):
    elemento=int(input('escreva o elemento:'))
    K.append(elemento)
X=degrais(K)
print(X)

         
