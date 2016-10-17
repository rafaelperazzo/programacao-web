# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite o valor de n:')
j=input('Digite o valor de j:')
k=input('Digite o valor de k:')
l=input('Digite o valor de l:')

if n==k and j!=l:
    print('verdadeira')
elif j==l and n!=k:
    print('verdadeira')
else:
    print('falsa')
if n==j or j==k or k==l:
    print('falso')