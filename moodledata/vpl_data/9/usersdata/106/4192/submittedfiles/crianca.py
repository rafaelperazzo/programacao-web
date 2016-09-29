# -*- coding: utf-8 -*-
from __future__ import division

#entrada 
p1 = input ('Digite o peso da criança 1:')
p2 = input ('Digite o peso da criança 2:')
c1 = input ('Digite o comprimento da gangorra do lado esquerdo:')
c2 = input ('Digite o comprimento da gangorra do lado direito:')

#processamento:
if p1*c1==p2*c2:
    print ('0')
elif p1*c1>p2*c2:
    print ('-1')
elif p1*c1<p2*c2:
    print ('1')