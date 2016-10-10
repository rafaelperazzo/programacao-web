# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input ('Digite a quantidade de múltiplos desejada:')
a = input ('Digite um número:')
b = input ('Digite um número:')

Soma = 0
i = 1
while Soma < n:
    if i%a == 0 or i%b==0:
        print (i)
        Soma = Soma + 1
    i = i+1