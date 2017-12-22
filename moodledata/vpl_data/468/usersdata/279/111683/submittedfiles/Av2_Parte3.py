# -*- coding: utf-8 -*-

m=(int(input()))
n=(int(input()))
matriz=[]
media=[]
a=0
for i in range(0,m,1) :
    lista=[]
    for i in range(0,n,1) :
        lista.append(float(input()))
        a=(a+lista[i])
    matriz.append(lista)
    media.append(a/n)
i=0 
matrizdesvio=[]
while(True) :    
    b=0
    for j in range(0,n,1) :
     b=(b+((matriz[i][j]-media[i])**2)) 
    desvio=((1/(n-1)*b)**(1/2))
    matrizdesvio.append(desvio)
    i=i+1
    desvio=0
    if i==m :
        break
for i in range(0,m,1) :
    print(%.2f %media[i])
    print(%.2f %matrizdesvio[i])
    

















































