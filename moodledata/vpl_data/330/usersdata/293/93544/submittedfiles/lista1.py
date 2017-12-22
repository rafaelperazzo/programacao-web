# -*- coding: utf-8 -*-

n=int(input("Digite n: "))
lista=[]
soma_impares=0
soma_pares=0
cont_pares=0
cont_impares=0

for i in range(0,n,1):
    lista.append(int(input("Digite o  valor da lista %d: " %(i+1))))

for i in range(0,n,1):
    if lista[i]%2!=0:
        soma_impares=lista[i]+soma_impares
print(soma_impares)

for i in range(0,n,1):
    if lista[i]%2==0:
        soma_pares=lista[i]+soma_pares
print(soma_pares)

for i in range(0,n,1):
    if lista[i]%2!=0:
        cont_impares=cont_impares+1
print(cont_impares)

for i in range(0,n,1):
    if lista[i]%2==0:
        cont_pares=cont_pares+1
print(cont_pares)