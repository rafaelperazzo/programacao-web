# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n= int(input('Digite a quantidade de elementos: '))
a=[]
soma1=0
soma2=0
for i in range (0,n,1):
    a.append(int(input('Digite o numero%: ' % (i+1))))
for i in range (0,n,1):
    soma1+=a[i]
    media=soma1/n
    soma2= (a[i]-media)**2
    d=((1/(n-1))*(soma2))**0.5
    
