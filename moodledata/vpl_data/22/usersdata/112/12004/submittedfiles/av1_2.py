# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite o valor de n:')
j=input('Digite o valor de j:')
k=input('Digite o valor de k:')
l=input('Digite o valor de l:')

if n==k and j!=l and n!=j and k!=l:
    print('V')
elif j==l and n!=k and k!=l and n!=j:
    print('V')
else:
    print('F')
