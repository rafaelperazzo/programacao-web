# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de numeros da lista: '))
entrada=int(input('Digite a porta de entrada: '))
saida=int(input('Digite a porta de saida: '))
a=[]
soma=0
 
for i in range(1,n+1,1):
    numero=int(input('Digite o numero de vidas para a sala: '))
    a.append(numero)
i=entrada
j=saida
while i<j:
    soma=soma+a[i]
    entrada=entrada+1

print(soma+a[j])

    


    


