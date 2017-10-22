# -*- coding: utf-8 -*-
import math

n = int(input("Digite quantos números N você quer imprimir: "))
a = int(input("Qual o seu número 'a'? "))
b = int(input("Qual o seu número 'b'? "))

for x in range(a, b):
    if x % n == 0:
        print(x)
    else:
        print('Inexistente')
