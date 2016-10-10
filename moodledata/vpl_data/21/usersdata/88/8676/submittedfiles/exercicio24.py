# -*- coding: utf-8 -*-
from __future__ import division
import math

a= input('digite um numero: ')
b= input('digete um numero: ')

resto=0
while (resto!=0):
    resto= a%b
    a=b
    b=resto
print b
