# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

#CONTINUE...

if a>b and a>c and a>d and a>e:
    print ("maior:%.d"%a)
if b>a and b>c and b>d and b>e:
    print ("maior:%.d"%b)
if c>a and c>b and c>d and c>e:
    print ("maior:%.d"%c)
if d>a and d>b and d>c and d>e:
    print ("maior:%.d"%d)
if e>a and e>b and e>c and e>d:
    print ("maior:%.d"%e)
if a<b and a<c and a<d and a<e:
    print ("menor:%.d"%a)
if b<a and b<c and b<d and b<e:
    print ("menor:%.d"%b)
if c<a and c<b and c<d and c<e:
    print ("menor:%.d"%c)
if d<a and d<b and d<c and d<e:
    print ("menor:%.d"%d)
if e<a and e<b and e<c and e<d:
    print ("menor:%.d"%e)
