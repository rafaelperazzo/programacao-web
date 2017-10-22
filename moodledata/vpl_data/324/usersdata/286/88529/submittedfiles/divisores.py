# -*- coding: utf-8 -*-
import math

n = int(input("Digite quantos números N você quer imprimir: "))
a = int(input("Qual o seu número 'a'? "))
b = int(input("Qual o seu número 'b'? "))

i = 0
for i in range(a, b + 1):
    if i % n == 0:
        print i
    
