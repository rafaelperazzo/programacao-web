# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de múltiplos: ')
a=input('Digite o primeiro número: ')
b=input('Digite o sesundo número: ')

x=1

while True:
    if x%a==0 or x%b==0:
        for i in range (0,n,1):
            print (x)
    x=x+1
        