# -*- coding: utf-8 -*-
from __future__ import division
import math
print('Para verificar a cobra, especifique valores entre 1 e 9 para representar cada cor observada')
a=input('Digite o valor para a primeira cor:')
b=input('Digite o valor para a segunda cor:')
c=input('Digite o valor para a terceira cor:')
d=input('Digite o valor para a quarta cor:')
if((a==c and b!=d) or (a!=c and b==d)):
    print('V')
else:
    print('F')