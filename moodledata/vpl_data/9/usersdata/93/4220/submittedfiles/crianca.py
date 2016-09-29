# -*- coding: utf-8 -*-
from __future__ import division
p1=input('peso da criança do lado esquerdo:')
c1=input('comprimentos da gangorra do lado esquerdo:')
p2=input('peso da criança do lado direito:')
c2=input('comprimentos da gangorra do lado direito:')
if p1*c1==p2*c2:
    print('0')
elif p1*c1>p2*c2:
    print('-1')
elif p1*c1<p2*c2:
    print('1')