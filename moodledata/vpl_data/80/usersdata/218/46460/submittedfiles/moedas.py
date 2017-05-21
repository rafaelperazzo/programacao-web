# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor a ser trocado:'))
i=0
resto=0
if a>=b:
    M=a
    m=b
else:
    M=b
    m=a
if M%c==0:
    print(c//M)
    print(0)
else:
    resto=c//M
    if resto%m==0:
        print(M//c)
        print(m//resto)
    