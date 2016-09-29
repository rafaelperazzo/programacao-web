# -*- coding: utf-8 -*-
from __future__ import division
import math

valor=input('Digite quanto deseja sacar:')
a=20
b=10
c=5
d=2
e=1

j=(valor//a)
r=(valor%a)
if r == 0:
    print('a= %.1d'% j)
else:
    k=(valor//b)
    l=(valor//d)
    m=(valor//e)
    print('b=%1d'% k 'c=%id'% l 'd=%1d%' m)