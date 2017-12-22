# -*- coding: utf-8 -*-
n=int(input("digite a quantidade de elementos nas listas: "))
listaA=[]
listaB=[]
listaC=[]

for i in range(0,n,1):
    listaA.append(int(input("digite um elemento para a listaA: ")))
for i in range(0,n,1):
    listaB.append(int(input("digite um elemento para a listaB: ")))
for i in range(0,n,1):
    listaC.append(int(input("digite um elemento para a listaC: ")))
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0

for i in range (0,n-1,1):
    if listaA[i]>listaA[i+1]:
        a+=1
    
for i in range (0,n-1,1):
    if listaA[i]<listaA[i+1]:
        b+=1
    
        
for i in range (0,n-1,1):
    if listaA[i]==listaA[i+1]:
        c+=1
        
if a==(n-1):
    print ("S")
else:
    print ("N")
    
        



