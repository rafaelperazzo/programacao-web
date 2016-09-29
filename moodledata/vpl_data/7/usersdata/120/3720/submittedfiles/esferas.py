# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
a=input('insira o valor do peso a:')
b=input('insira o valor do peso b:')
c=input('insira o valor do peco c:')
d=input('insira o valor do peso d:')
#PROCESSAMENTO
if a==b+c+d and b+c==d and b==c:
    print ('S')
else:
    print ('N')