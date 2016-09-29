# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite o numero de vitorias de C: ')
b=input('Digite o numero de empates de C: ')
c=input('Digite o saldo de gols de C: ')
d=input('Digite o numero de vitorias de D: ')
e=input('Digite o numero de empates de D: ')
f=input('Digite o saldo de gols de D: ')

g=((a*3) + (1*b)) 
h=((d*3) + (1*b)) 

if g>h:
    print 'C'
if h>g:
    print 'F'
if g==h and c>f:
    print 'C'
if g==h and f>c:
    print 'F'
if g==h and c==f:
    print '='
    

    