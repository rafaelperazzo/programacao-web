# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de numeros da lista: '))
i=int(input('Digite a porta de entrada: '))
j=int(input('Digite a porta de saida: '))
a=[]
soma=0
 
for i in range(1,n+1,1):
    numero=int(input('Digite o numero de vidas para a sala: '))
    a.append(numero)


while i<j:
    soma=soma+a[i]
    i=i+1

print(soma+a[j])

    


    


