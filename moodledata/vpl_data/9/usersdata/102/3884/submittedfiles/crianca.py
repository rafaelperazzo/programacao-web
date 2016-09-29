# -*- coding: utf-8 -*-
from __future__ import division
p1=input('peso da criança 1:')
p2=input('peso da criança 2:')
c1=input('comprimento da gangorra do lado direito')
c2=input('comprimento da gangorra do lado esquerdo')

if (p1*c1)==(p2*c2):
    print('0')
    
elif (p1*c1)>(p2*c2):
    print('-1')
    
elif (p1*c1)<(p2*c2) :
    print('1')