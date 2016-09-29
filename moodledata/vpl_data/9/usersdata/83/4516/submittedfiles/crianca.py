# -*- coding: utf-8 -*-
from __future__ import division

p1=input('Peso da criança a esquerda: ')
c1=input('Comprimento da parte esquerda da gangorra: ')
p2=input('Peso da criança a direita: ')
c2=input('Comprimento da parte direita da gangorra: ')

if p1*c1==p2*c2 :
    print ('0')
elif p1*c1>p2*c2 :
    print ('-1')
elif p1*c1<p2*c2 :
    print ('1')
    