# -*- coding: utf-8 -*-
from __future__ import division

p1 = input ('Digite o peso da criança da esquerda:')
p2 = input ('Digite o peso da criança da direita:')
c1 = input ('Digite o valor do comprimento esquerdo:')
c2 = input ('Digite o valor do comprimento direito:')

if ((p1*c1)==(p2*c2)):
    print ('0')
elif ((p1*c1)>(p2*c2)):
    print ('1')
elif ((p1*c1)<(p2*c2)):
    print ('2')
