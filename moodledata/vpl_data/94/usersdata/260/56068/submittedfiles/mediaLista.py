# -*- coding: utf-8 -*-
n=int(input("digite o tamanho da lista "))
lista=[]
media=0
for i in range(0,n,1):
    lista.append(float(input("digite o primeiro valor ")))
    media=media+lista[i]
media=media/(len(lista))
print("%.2f" %lista[0])
print("%.2f" %lista[n-1])
print("%.2f" %media)
print("%.2f" %lista)
