# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input("digite o tamanho da lista:"))
lista=[]
media=0
s=0
s1=0
for i in range(0,n,1):
    lista.append(int(input("digite o valor do elemento:")))
    media=media+lista[i]
media=media/len(lista)
for i in range(0,len(lista),1):
    s1=s1+(lista[i]-media)**2
s=s1*1/(n-1)
s=s**(1/2)
print("%.2f" %lista[0])
print("%.2f" %lista[i])
print("%.2f" %media)
print("%.2f" %s)