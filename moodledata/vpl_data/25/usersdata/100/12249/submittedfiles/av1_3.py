# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('numero 1:')
b=input('numero 2:')
s=0
c=1
x=1
""" Para tanto teremos que o processo de divisão do resto pelo divisor antecessor, do tipo:
1320/35 = 25(resto) dividido por 35, depois 35/quociente(25)
= resto (10) """
while x<a :
    a= a%b
    b=a%b
    print a