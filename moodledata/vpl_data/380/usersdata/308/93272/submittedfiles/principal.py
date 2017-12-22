# -*- coding: utf-8 -*-
from minha_bib import *
from random import randint

notas = sorteiaReaisVetor(10, 2)

for i in range (len(notas), 0, -1):
    print(notas[i-1])
        
    