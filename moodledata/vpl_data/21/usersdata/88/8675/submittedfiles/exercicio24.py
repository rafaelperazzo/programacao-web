# -*- coding: utf-8 -*-
from __future__ import division
import math

a= input('digite um numero: ')
b= input('digete um numero: ')

resto=a%b
while (resto!=0):
    a=b
    b=resto
print b
