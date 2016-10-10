# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de divisores: :')
a=input('Digite a: ')
b=input('Digite b: ')

i=2
contador=0

while (contador<n):
    if (a%i==0 or b%i==0):
        print(i)
        contador=contador+1
    i=i+1