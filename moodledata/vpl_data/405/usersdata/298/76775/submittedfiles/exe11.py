# -*- coding: utf-8 -*-
m = '420'.split()
print(m)

numero = input('Digite um número: ')
separar = numero.split()
algarismos = [int(n) for n in separar]

for n in algarismos:
    if type(n) == int:
        a, b, c, d, e, f, g, h = algarismos
        soma= a+b+c+d+e+f+g+h
        print(soma)
    else:
        print('NAO SEI')

#testar antes
