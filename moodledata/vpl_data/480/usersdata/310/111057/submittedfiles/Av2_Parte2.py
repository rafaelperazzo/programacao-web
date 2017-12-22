# -*- coding: utf-8 -*-
#Soma é o resultado da soma de todos os algarismos do número recebido

a=int(input('digite a: '))
if a>0 and a<10:
    print(a)
elif a>10 and a<100:
    soma=(a//10) + (a%10)
    print(soma)
elif a>9 and a<11:
    print(1)
elif a>99 and a<101:
    print(1)
elif a>999 and a<1001:
    print(1)
elif a>9999 and a<10001:
    print(1)