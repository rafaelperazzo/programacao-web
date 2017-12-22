# -*- coding: utf-8 -*-
#Soma é o resultado da soma de todos os algarismos do número recebido

a = int(input('Digte a: '))
if a>0 and a<=10:
    soma=print(a%10)
elif a>10 and a<100:
    soma=(a//10)+(a%10)
    print(soma)
elif a>=100 and a<=1000:
    soma=(a//100)+((a%100)//10)+((a%100)//10)
    print(soma)

        