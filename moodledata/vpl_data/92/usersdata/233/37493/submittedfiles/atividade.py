# -*- coding: utf-8 -*-
import math
n=int(input('Digite um valor para n: '))
soma=0
termo=1
numerador=1
denominador=n
while termo<=n:
    soma=soma+numerador/denominador
    termo=termo+1
    denominador=denominador-1
    