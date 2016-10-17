# -*- coding: utf-8 -*-
from __future__ import division
import math

n1 = input('Digite o número 1:')
n2 = input('Digite o número 2:')
#a/b=c & a%b=r

if n1>n2:
    m1=n1
elif n2>n1:
    m1=n2
else:
    m1=n1
m2 = m1

cont = 0
r = (a%b)
while r!=0:
    b=a
    r=b
    cont=cont+1
    if r>m1 and m1!=0:
        m1=r