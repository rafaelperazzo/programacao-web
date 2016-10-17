# -*- coding: utf-8 -*-
from __future__ import division
import math

n1= input('Digite n1: ')
n2= input('Digite n2: ')

cont1=0
while n1>=1:
    cont1= cont1+1
    n1= n1/10

cont2=0
while n2!=int(n2):
    cont2= cont2+1
    n2= n2*10

print(cont1)
print(cont2)
