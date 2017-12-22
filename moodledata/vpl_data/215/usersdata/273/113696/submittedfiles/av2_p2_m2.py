# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de numeros da lista: '))
en=int(input('Digite a porta de entrada: '))
sa=int(input('Digite a porta de saida: '))
lista=[]
soma=0
 
for i in range(1,n+1,1):
    a=int(input('Digite o numero de vidas para a sala: '))
    lista.append(a)
    
while (en<sa):
    soma=soma+lista[en]+lista[sa]
    entrada=entrada+1
    
print(soma)
    


    


