# -*- coding: utf-8 -*-
from __future__ import division

#Entrada
P1=input('Digite o peso da criança que está do lado esquerdo:')
C1=input('Digite o comprimento da gangorra do lado esquerdo:')
P2=input('Digite o peso da criança que está do lado direito:')
C2=input('Digite o comprimento da gangorra do lado direito:')

if (P1*C1==P2*C2):
    print ('0')
    
if (P1*C1<P2*C2):
    print ('-1')
    
if (P1*C1>P2*C2):
    print ('1')