# -*- coding: utf-8 -*-
na=int(input('tamanho de a:'))
nb=int(input('tamanho de b:'))
A=[]
B=[]
cont=0
for i in range (1,na+1,1):
    a=int(input('elemento de a: '))
    A.append(a)
for i in range (1,nb+1,1):
    b=int(input('elemento de b: '))
    B.append(b)
for i in range (0,len(A),1):
    for i in range (0,len(B),1):
        if A[i]==B[i]:
            cont=cont+1
print(cont)