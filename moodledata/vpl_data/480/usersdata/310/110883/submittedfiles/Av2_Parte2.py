# -*- coding: utf-8 -*-
#Soma é o resultado da soma de todos os algarismos do número recebido

a = int(input('Digite a: '))
cont=0
while a>0:
    soma=(a//10)+(a%10)
    print(soma)