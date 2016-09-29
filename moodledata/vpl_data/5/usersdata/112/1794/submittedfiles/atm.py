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
J1=(valor%a)
k=(valor//b)
k1=(valor%b)
l=(valor//d)
L1=(valor&d)
m=(valor//e)
M1=(valor%e)

if J1 == 0:
    print(j,k,l)