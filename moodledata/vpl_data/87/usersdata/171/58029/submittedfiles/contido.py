# -*- coding: utf-8 -*-
def quantidade(lista1,lista2):
    cont=0
    for i in range(0,len(lista),1):
        if lista1[i]==lista2[i]:
            cont=cont+1
    return(cont)
n=int(input('digite o numero de elemento:'))
lista1=[]
for i in range(1,n+1,1):
    valor1=float(input('digite o numero á ser colocado na lista 1:'))
    lista1.append(valor1)
n=int(input('digite o numero de elemento:'))
lista2=[]
for i in range(1,n+1,1):
    valor2=float(input('digite o numero á ser colocado na lista 2:'))
    lista2.append(valor2)
if quantidade(lista1,lista2):
    print(quantidade(lista1,lista2))

