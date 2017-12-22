# -*- coding: utf-8 -*-
#Soma é o resultado da soma de todos os algarismos do número recebido

a = int(input('Digte a: '))
if a<=10:
    print(a)
elif a<=100:
    soma=(a//10)+(a%10)
    print(soma)
elif a <=1000:
    soma=(a//10)+(a%10)
        