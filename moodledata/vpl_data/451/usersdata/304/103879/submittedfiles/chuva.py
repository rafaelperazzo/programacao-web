# -*- coding: utf-8 -*-

n = int(input('Digite o vão: '))
lista = []
for i in range(0,n,1):
    lista.append(int(input('Digite a altura: ')))
for i in range(0,len(lista),1):
    soma=0
    if lista[i]>=lista[i+1]:
        soma = soma+(lista[i]-lista[i+1])
    else:
        break
    print(soma)



