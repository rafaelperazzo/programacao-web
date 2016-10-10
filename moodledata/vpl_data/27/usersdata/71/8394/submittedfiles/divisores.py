# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input("Insira o Número de Divisores: ")
a = input("Insira um Número: ")
b = input("Insira outro Número: ")

divisor = 0
i = 1

while True:
    if i%a==0 or i%b==0:
        print i
        divisor=divisor+1
    if divisor==n:
        break
    i=i+1