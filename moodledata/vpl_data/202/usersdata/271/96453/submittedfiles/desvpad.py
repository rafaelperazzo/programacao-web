# -*- coding: utf-8 -*-
import math

#comece abaixo
#ENTRADA
n = int(input('Digite a quantidade de valores : '))
a = []
#PROCESSAMENTO
for i in range (0,n,1) :
    valor = int(input('Digite o valor : '))
    a.append(valor)
def media(x) :
    soma = 0
    for i in range (0,len(a),1) :
        valorm = a[i]
        soma = soma+valorm
    media = soma/n
    return(media)
#SAIDA

        

