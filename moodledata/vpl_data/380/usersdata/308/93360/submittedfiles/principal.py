# -*- coding: utf-8 -*-
from minha_bib import *
from random import randint
import time
n = int(input('Informe a quantidade de valores: '))

#valores = sorteiaReaisVetor(n, 2)
valores = [1, 2, 3, 4]
print(valores)

dmh = 0
for i in range (0, n):
    dmh += 1/valores[i]
    time.sleep(1)
    print('1/%.2f' % valores[i])
print(len(valores)/dmh)