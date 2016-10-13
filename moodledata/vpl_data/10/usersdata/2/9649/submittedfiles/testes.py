# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#COMECE AQUI ABAIXO
n = input('Digite n: ')
m = input('Digite o valor de m: ')

#Contar digitos de m
cont = 0
temp = m
while temp>0:
    temp = temp//10
    cont = cont + 1
print cont
