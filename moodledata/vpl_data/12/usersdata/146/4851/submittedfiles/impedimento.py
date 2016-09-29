# -*- coding: utf-8 -*-
from __future__ import division
import math

l = input('DIGITE O VALOR DE L: ')
r = input('DIGITE O VALOR DE R: ')
d = input('DIGITE O VALOR DE D: ')

if r<50 or r<d or r<l:
    print 'N'

elif r>d>50:
    print 'S'