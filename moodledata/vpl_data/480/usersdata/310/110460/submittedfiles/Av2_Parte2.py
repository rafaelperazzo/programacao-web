# -*- coding: utf-8 -*-

a = int(input('Digte a: '))
if a<=10:
    print(a)
elif a<=100:
    soma=(a//10)+(a%10)
    print(soma)