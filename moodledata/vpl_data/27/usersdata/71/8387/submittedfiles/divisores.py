# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input("Insira o Número de Divisores: ")
a = input("Insira um Número")
b = input("Insira outro Número")

contador = 0

for i in range (1,n+1,1):
    if i%a==0 or i%b==0:
        print i
        contador=contador+1
    i=i+1
