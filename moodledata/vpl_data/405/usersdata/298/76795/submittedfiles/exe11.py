# -*- coding: utf-8 -*-
numero = str(input('Digite um número: '))
k = map(int, str(numero))

for digit in k:
    if type(digit) == int:
        a, b, c, d, e, f, g, h = k
        soma= a+b+c+d+e+f+g+h
        print(soma)
    else:
        print('NAO SEI')

#testar antes
