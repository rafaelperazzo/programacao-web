# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite o valor da quantidade de valores de n:'))

contador=0
i=0

while i<=n:
    l=input('Digite o valores dos termos de n:')
    contador=contador+l
i=i+1

while i<=n:
    media=contador/n
    
    print(contador)