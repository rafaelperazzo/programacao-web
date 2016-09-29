# -*- coding: utf-8 -*-
from __future__ import division

P1= input('peso da criança lado esquerdo: ')
P2= input('peso da criança lado direito: ')
C1= input('comprimento da gangorra LD: ')
C2= input('comprimento da gangorra LE: ')

(P1*C1)=(P2*C2)

if (P1*C1)==(P2*C2):
    print('0')
if (P1*C1)<(P2*C2):
    print('-1')
if (P1*C1)>(P2*C2):
    print('1')
    
