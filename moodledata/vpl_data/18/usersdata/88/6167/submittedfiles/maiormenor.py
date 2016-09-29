# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

if a<b<c<d<e:
    print('%f' %a)
    print('%f' %e)
if b<a<c<d<e:
    print('%f' %b)
    print('%f' %e)
if c<b<a<d<e:
    print('%f' %c)
    print('%f' %e)
if d<c<b<a<e:
    print('%f' %d)
    print('%f' %e)
if e<d<c<b<a:
    print('%f' %e)
    print('%f' %a)
    
