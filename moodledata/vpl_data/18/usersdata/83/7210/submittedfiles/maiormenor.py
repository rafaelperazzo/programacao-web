# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

if a>b and a>c and a>d and a>e :
    print ('O maior numero é o %f' %a)
elif b>a and b>c and b>d and b>e :
    print ('O maior numero é o %f' %b)
elif c>b and c>a and c>d and c>e :
    print ('O maior numero é o %f' %c)
elif d>b and d>c and d>a and d>e :
    print ('O maior numero é o %f' %d)
elif e>b and e>c and e>d and e>a :
    print ('O maior numero é o %f' %e)
if a<b and a<c and a<d and a<e :
    print ('O menor numero é o %f' %a)
elif b<a and b<c and b<d and b<e :
    print ('O menor numero é o %f' %b)
elif c<b and c<a and c<d and c<e :
    print ('O menor numero é o %f' %c)
elif d<b and d<c and d<a and d<e :
    print ('O menor numero é o %f' %d)
elif e<b and e<c and e<d and e<a :
    print ('O menor numero é o %f' %e)