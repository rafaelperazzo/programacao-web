# -*- coding: utf-8 -*-
from __future__ import division
n = input('Digite n: ')

cont = 0

for i in range(1,n+1,1):

    if n% i ==0:

        cont = cont +  1

if cont==2  :

    print('primo  ')

else:

    print('nao e primo  ')
 