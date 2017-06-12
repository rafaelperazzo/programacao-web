# -*- coding: utf-8 -*-
n=int(input('digite n:'))
m=int(input('digite m:'))
lista1=[]
lista2=[]
cont=0
for i in range(0,n,1):
    valor1=int(input('digite valor 1:'))
    lista1.append(valor1)
for i in range(0,n,1):
    valor2=int(input('digite valor 2:'))
    lista2.append(valor2)
for x in range(0,len(lista1),1):
    for y in range(0,len(lista2),1):
        if a[x]==b[y]:
            cont=cont+1
print(cont)

