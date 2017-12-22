# -*- coding: utf-8 -*-
#ENTRADA
n = int(input('Digite a quantidade de valores da lista : '))
a = []
#PROCESSAMENTO
for i in range (0,n,1) :
    valor = int(input('Digite o valor : '))
    a.append(valor)
def media(x) :
    soma = 0
    for i in range (0,len(a),1) :
        valorm = a[i]
        soma = soma + valorm
    media = soma/n
    return (media)
#SAIDA
print(a[0])
print(a[n-1])
print(media(x))




