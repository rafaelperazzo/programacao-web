# -*- coding: utf-8 -*-

n = int(input('Digite o vão: '))
lista = []
for i in range(0,n,1):
    lista.append(int(input('Digite a altura: ')))
    
for i in range(0,len(lista),1):
    if lista[0]>=lista[i]:
        soma=0
        soma = soma+(lista[0]-lista[i])
    else:
        break
    print(soma)



