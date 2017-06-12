# -*- coding: utf-8 -*-
n=int(input('Informe o número de elementos da primeira lista:'))
m=int(input('Informe o número de elementos da segunda lista:'))
lita1=[]
lista2=[]

for i in range(1,n+1,1):
    numero=int(input('Informe um número:'))
    lista1.append(numero)
    
for i in range(1,m+1,1):
    numero=int(input('Informe um número:'))
    lista2.append(numero)

def nao_pertence(lista1,lista2):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i] not in lista2:
            cont=cont+1
print(cont)
        