# -*- coding: utf-8 -*-
from __future__ import division
import math

i=input('Digite um número inteiro maior ou igual a 1: ')
r=input('Digite um número real entre 0 e 1: ')

nI=i
contI=0

while nI>=1:
    nI=nI//10
    contI=contI+1
print contI

nR=r
contR=0

while True:
    nR=nR*10
    contR=contR+1
    if :nR%10==0:
        break
    print contR
