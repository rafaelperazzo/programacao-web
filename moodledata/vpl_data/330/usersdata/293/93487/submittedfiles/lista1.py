# -*- coding: utf-8 -*-

n=int(input("Digite n: "))
lista=[]
for i in range(0,n,1):
    lista.append(int(input("Digite o  valor da lista %d: " %(i+1))))
soma_pares=0
for i in range(0,n,1):
    if lista[i]%2==0:
        soma_pares=lista[i]+soma_pares
    print(soma_pares)

    

