# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

if a < b <= c <= d <= e:
    print str(a)
    print str(e)
    
    
if b < a <= b <= d <= e:
    print str(c)
    print str(e)
if c < b <= a <= d <= e:
    print str(c)
    print str(e)
if c < d <= a <= b <= e:
    print str(c)
    print str(e)
if c < e <= a <= b <= d:
    print str(c)
    print str(d)
    
    
if c < a <= b <= d <= e:
    print str(c)
    print str(e)
if c < b <= a <= d <= e:
    print str(c)
    print str(e)
if c < d <= a <= b <= e:
    print str(c)
    print str(e)
if c < e <= a <= b <= d:
    print str(c)
    print str(d)
    
