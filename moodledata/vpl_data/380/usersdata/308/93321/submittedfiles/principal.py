# -*- coding: utf-8 -*-
from minha_bib import *
from random import randint

n = int(input('Informe a quantidade de valores: '))

valores = sorteiaReaisVetor(n, 2)
print(valores)

dmh = 0
for i in range (0, n):
    dmh += 1/valores[i]

print(len(valores)/dmh)