# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de múltiplos: ')
a=input('Digite o primeiro número: ')
b=input('Digite o sesundo número: ')

i=1
cont=0

while True:
    if i%a==0 or i%b==0:
        print (i)
        cont=cont+1
    i=i+1
    
    if cont==n:
        break