# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#ENTRADA
n = int(input("Digite o valor de n: "))
a = []
for i in range(0,n,1):
    a.append(int(input('Digite um valor: ')))
soma = 0
for i in range(0,n,1):
    soma = soma + 1
    media = (soma/n)
print(media)
    
