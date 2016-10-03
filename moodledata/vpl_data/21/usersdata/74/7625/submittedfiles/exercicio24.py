# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))

i = 1
cont = 0

while i>=a or i>=b:
    if a%i==0:
        mdca = a/i
    if b%i==0:
        mdcb = b/i
    if mdca == mdcb:
        cont = mdca
    
    i=i+1
    print('%d'% cont)