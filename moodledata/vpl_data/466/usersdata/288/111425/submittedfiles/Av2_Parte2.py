# -*- coding: utf-8 -*-
n=int(input("digite a quantidade de elementos nas listas: "))
listaA=[]
listaB=[]
listaC=[]

for i in ranfe(0,n,1):
    listaA.append(int(input("digite um elemento para a listaA: ")))
    listaB.append(int(input("digite um elemento para a listaB: ")))
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
        continue
    else:
        a+=1
    if listaA[i]<listaA[i+1]:
        continue
    else:
        b+=1
    if listaA[i]==listaA[i+1]:
        continue
    else:
        c+=1
        
for i in range (0,n-1,1):
    if listaB[i]>listaB[i+1]:
        continue
    else:
        d+=1
    if listaB[i]<listaB[i+1]:
        continue
    else:
        e+=1
    if listaB[i]==listaB[i+1]:
        continue
    else:
        e+=1
for i in range (0,n-1,1):
    if listaC[i]>listaC[i+1]:
        continue
    else:
        f+=1
    if listaC[i]<listaC[i+1]:
        continue
    else:
        g+=1
    if listaC[i]==listaC[i+1]:
        continue
    else:
        h+=1
if a==0:
    print ("S")
else:
    print ("N")
if b==0:
    print ("S")
else:
    print ("N")
if c==0:
    print ("S")
else:
    print ("N")
if d==0:
    print ("S")
else:
    print ("N")
if e==0:
    print ("S")
else:
    print ("N")
if f==0:
    print ("S")
else:
    print ("N")
if g==0:
    print ("S")
else:
       print ("N")
if h==0:
    print ("S")
else:
    print ("N")
   