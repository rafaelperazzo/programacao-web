# -*- coding: utf-8 -*-
from __future__ import division
import math

n= input ('digite o valor para n: ')

while n>0:
    x= input ('digite o valor de x: ')
    y= input ('digite o valor de y: ')
    if x>=0 and y>=0 and ((x**2)+(y**2))<=1:
        print 'SIM'
    else:
        print 'NAO'
    n=n-1
    