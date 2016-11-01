# -*- coding: utf-8 -*-
from __future__ import division

p=int(input('digite o valor de p:'))
q=int(input('digite o valor de q:'))

contadorp=0
contadorq=0
contador=0
i=p

while i>0:
    i=i//10
    contadorp=contadorp+1
