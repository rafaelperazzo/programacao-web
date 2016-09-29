# -*- coding: utf-8 -*-
from __future__ import division
p1=input('peso da criança p1:')
c1=input('comprimento da gangorra do lado direito c1:')
p2=input('peso da criança p2:')
c2=input('comprimento da gangorra do lado esquerdoc2:')

if p1*c1==p2*c2:
    print('0')
    
elif p1*c1>p2*c2:
    print('-1')
    
elif p1*c1<p2*c2:
    print('1')
    