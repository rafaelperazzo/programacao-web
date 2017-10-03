# -*- coding: utf-8 -*-
numero = input('Digite um número: ')
separar = split.numero()
algarismos = [int(n) for n in numero]

for n in algarismos:
    if type(n) == int:
        a, b, c, d, e, f, g, h = algarismos
        soma= a+b+c+d+e+f+g+h
        print(soma)
    else:
        print('NAO SEI')


