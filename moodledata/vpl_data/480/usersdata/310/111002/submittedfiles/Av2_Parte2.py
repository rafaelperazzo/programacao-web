# -*- coding: utf-8 -*-
#Soma é o resultado da soma de todos os algarismos do número recebido

a=int(input('digite a: '))
if a>0 and a<10:
    print(a)
elif a>10 and a<100:
    soma=(a//10) + (a%10)
    print(soma)