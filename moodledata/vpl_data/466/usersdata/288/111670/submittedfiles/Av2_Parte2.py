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
    if listaA[i]<listaA[i+1]:
        a+=1
    
    if listaA[i]>listaA[i+1]:
        b+=1
    
    if listaA[i]==listaA[i+1]:
        c+=1
        
for i in range (0,n-1,1):
    if listaB[i]<listaB[i+1]:
        d+=1
    
    if listaB[i]>listaB[i+1]:
        e+=1
    
    if listaA[i]==listaA[i+1]:
        f+=1

for i in range (0,n-1,1):
    if listaC[i]<listaC[i+1]:
        g+=1
    
    if listaC[i]>listaC[i+1]:
        h+=1
    
    if listaC[i]==listaC[i+1]:        
        i+=1
if a==(n-1):
    print ("S")
else:
    print ("N")
    
if b==(n-1):
    print ("S")
else:
    print ("N")
    
if c>=1:
    print ("S")
else:
    print ("N")
    
if d==(n-1):
    print ("S")
else:
    print ("N")
    
if e==(n-1):
    print ("S")
else:
    print ("N")
    
if f>=1:
    print ("S")
else:
    print ("N")
    
if g==(n-1):
    print ("S")
else:
    print ("N")
    
if h==(n-1):
    print ("S")
else:
    print ("N")
    
if i>=1:
    print ("S")
else:
    print ("N")



