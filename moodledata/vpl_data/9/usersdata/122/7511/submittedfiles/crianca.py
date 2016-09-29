# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA

pa=input ('Digite o valor de pa:')
pb=input ('Digite o valor de pb:')
ca=input ('Digite o valor de ca:')
cb=input ('Digite o valor de cb:')

#PROCESSAMENTO

if (pa*ca)=(pb*cb):
    print('0')
elif(pa*ca)<(pb*cb):
    print('-1')
elif(pa*ca)*(pb*cb):
    print('1')