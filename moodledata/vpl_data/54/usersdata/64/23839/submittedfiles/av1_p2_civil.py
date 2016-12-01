# -*- coding: utf-8 -*-
from __future__ import division

n=input("Digite a quantidade de pinos da fechadura: ")
m=input("Digite a altura que o pino deve ficar: ")

i= 1
a=[]

while i<=n:
    lista.append(input("Digite o tamanho do pino: "))
    i=i+1
    
j=0
contador=0

while j<(n-1):
    while a[j]>m and a[j+1]>m:
        a[j]=a[j]-1
        a[j+1]=a[j+1]-1
        contador=contador+1
        
    while a[j]<m and a[j+1]<m:
        a[j]=a[j]+1
        a[j+1]=a[j+1]+1
        contador=contador+1
        
    while a[j]>m:
        a[j]=a[j]-1
        contador=contador+1   
    while a[j]<m:
        a[j]=a[j]+1
        contador=contador+1
    
    j=j+1
    
if a[j]!=m:
    while a[j]>m:
        a[j] = a[j]-1
        contador = contador +1
    while a[j]<m:
        a[j]=a[j]+1
        contador= contador+1
        
print contador
print a