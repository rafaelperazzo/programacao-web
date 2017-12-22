# -*- coding: utf-8 -*-

while(True):
    m=(int(input()))
    if m>=2 and m<=2000 :
        break
while(True) :
    n=(int(input()))
    if n>=2 and n<=2000 :
        break
matriz=[]    
for i in range(0,m,1) :
    lista=[]
    for j in range(0,n,1) :
       lista.append(int(input()))
    matriz.append(lista)
i=0 
soma=[]

a=0
while(True):
    for j in range(0,n,1) :
        a=a+matriz[i][j]
       
    soma.append(a)
    i=i+1
    a=0
    if i==m :
        break
j=0
b=0
while(True) :
    for i in range(0,m,1) :
        b=b+matriz[i][j]
    
    soma.append(b)
    j=j+1
    b=0
    if j==n :
        break
c=soma[0]
for i in range(0,m+n,1) :
    if soma[i]<=c :
      c=soma[i]  
print(c)     























