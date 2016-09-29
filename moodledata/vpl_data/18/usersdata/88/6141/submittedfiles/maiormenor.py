# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

if a<b<c<d<e:
    print('%d' %a)
    print('%d' %e)
if b<a<c<d<e:
    print('%d' %b)
    print('%d' %e)
if c<b<a<d<e:
    print('%d' %c)
    print('%d' %e)
if d<c<b<a<e:
    print('%d' %d)
    print('%d' %e)
if e<d<c<b<a:
    print('%d' %e)
    print('%d' %a)
    
