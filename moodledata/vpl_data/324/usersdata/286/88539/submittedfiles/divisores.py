# -*- coding: utf-8 -*-
import math

n = int(input("Digite quantos números N você quer imprimir: "))
a = int(input("Qual o seu primeiro número? "))
b = int(input("Qual o seu segundo número? "))

h = 1
f = 1

while (f<=n):
    if h%a ==0 or h%b == 0:
        print(h)
        f += 1
    h += 1
