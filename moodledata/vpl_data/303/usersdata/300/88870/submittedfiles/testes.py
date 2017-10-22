# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
x = int(input('Digite um número com 8 algarismos: '))
if 9999999 < x < 100000000:
    a = 0
    while (x != 0):
        b = x%10
        x = (x-b)//10
        a = a + b
    print(a)
else:
    print('NAO SEI')