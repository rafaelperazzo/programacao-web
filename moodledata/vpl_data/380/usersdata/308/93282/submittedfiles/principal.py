# -*- coding: utf-8 -*-
from minha_bib import *
from random import randint

valores = sorteiaReaisVetor(10, 2)

dmh = 0
for i in range (0, n-1):
    dmh += 1/valores[i]

print(len(valores)/dmh)