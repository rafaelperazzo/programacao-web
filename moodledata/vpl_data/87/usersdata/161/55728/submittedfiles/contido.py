# -*- coding: utf-8 -*-
n=int(input('Informe o número de elementos da primeira lista:'))
m=int(input('Informe o número de elementos da segunda lista:'))
lista_a=[]
lista_b=[]

for i in range(1,n+1,1):
    numero=int(input('Informe um número:'))
    lista_a.append(numero)
    
for i in range(1,m+1,1):
    numero=int(input('Informe um número:'))
    lista_b.append(numero)

def nao_pertence(lista_a,lista_b):
    cont=0
    for i in range(0,len(lista),1):
        if lista_b[i] not in lista_a:
            cont=cont+1
    return (True,cont)            
print(nao_pertence[1])
        