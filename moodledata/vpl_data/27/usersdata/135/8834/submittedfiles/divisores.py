# -*- coding: utf-8 -*-
from __future__ import division
import math

h= input ('digite a quantidade de divisores desejados: ')
a= int(input('digite o valor de a: '))
b= int(input('digite o valor de b:' ))
c= 1

while h>0:
    if c%a==0 or c%b==0:
        print c
        h= n-1
    c= c+ 1
