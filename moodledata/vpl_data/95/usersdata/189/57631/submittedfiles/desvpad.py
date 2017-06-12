# -*- coding: utf-8 -*-
import math
lista=[]
n=int(input('digite o numero:'))
for i in range(0,n,1):
    numero=int(input('digite um nemuro:'))
    lista.append(numero)
    
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
    media=soma/len(lista)
    
soma1=0
for i in range(0,len(lista),1):
    soma1=soma1+(lista[i]-media(lista))**2
desvio=(soma1/(lenlista)-1)**0.5
print('%2.f' %lista[0])
print('%2.f' %lista[n-1])
print('%2.f' %media)
print('%2.f' %desvio)
    
    
