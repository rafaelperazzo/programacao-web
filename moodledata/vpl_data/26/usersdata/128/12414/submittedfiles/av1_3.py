# -*- coding: utf-8 -*-
from __future__ import division
import math

i=input('Digite um número inteiro maior ou igual a 1: ')
r=input('Digite um número real entre 0 e 1: ')

contI=0

while i>=1:
    i=i//10
    contI=contI+1
print contI

contR=0

while r-(r/10)!=0:
    r=r*10
    contR=contR+1
print contR
