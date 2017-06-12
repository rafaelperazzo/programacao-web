# -*- coding: utf-8 -*-
A=[]
B=[]
cont=0
for i in range (1,n+1,1):
    a=int(input('elemento de a: '))
    A.append(a)
for i in range (1,n+1,1):
    b=int(input('elemento de b: '))
    B.append(b)
for i in range (0,len(A),1):
    for i in range (0,len(b),1):
        if A[i]==B[i]:
            cont=cont+1
print(cont)