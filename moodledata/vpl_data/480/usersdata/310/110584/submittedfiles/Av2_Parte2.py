# -*- coding: utf-8 -*-
#Soma é o resultado da soma de todos os algarismos do número recebido

a = int(input('Digte a: '))
if a>0 and a<=10:
    soma=print(a)
else:
    print('este número não é maior do que 0')
elif a>10 and a<=100:
    soma=(a//10)+(a%10)
    print(soma)


        