# -*- coding: utf-8 -*-
from __future__ import division
import math

n= int(input('Insira n:'))
a= int(input('Insira um valor para a:'))
b= int(input('Insira um valor para b:'))

cont=0
m=1
while cont<n:
    if (m%a)==0 or (m%b)==0:
        print m
        cont= cont+1
    m=m+1