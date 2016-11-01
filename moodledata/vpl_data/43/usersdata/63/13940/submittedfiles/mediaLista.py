# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('digite a quantidade de n:'))
contador=0
i=0
while i<=n:
    l=(input('digite o numero de termos:'))
    contador=contador+l
i=i+1

while i<=n:
    media=contador/n
    print(contador)