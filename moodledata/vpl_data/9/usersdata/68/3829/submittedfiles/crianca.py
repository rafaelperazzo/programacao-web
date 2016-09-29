# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA:
p1= ('Digite o peso da criança do lado esquerdo:')
c1= ('Digite o comprimento da gangorra do lado esquerdo:')
p2= ('Digite o peso da criança do lado direito:')
c2= ('Digite o comprimento da gangorra do lado direito:')

if p1*c1==p2*c2:
    print ('0')
if p1*c1>= p2*c2:
    print ('-1')
if p1*c1<= p2*c2:
    print ('1')