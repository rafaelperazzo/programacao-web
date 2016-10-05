# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#COMECE AQUI ABAIXO

n = input('Digite o valor de n:')
maior = 1
cont = 1
numero = input('Digite um numero: ')
for i in range(0,n,1):
    proximo = input('Digite um numero: ')
    if proximo>numero:
        cont = cont + 1
    else:
        cont = 1
    if cont>maior:
        maior = cont

print maior

