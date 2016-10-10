# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
while (a==0 or b==0):
   print('a ou b não podem ser zero')
   a=input('Digite o valor de a:')
   b=input('Digite o valor de b:')

r= int (a%b)
while r!=0:
    a=b
    b=r
    r=a%b
print (b)