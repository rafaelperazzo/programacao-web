# -*- coding: utf-8 -*-
from __future__ import division

from __future__ import division

p=input('Insira P: ')
q=input('Insira Q: ')

pp=p
contP=0

while pp>=1:
    pp=pp/10
    contP=contP+1

while True:
    if q%(10**contP)==p:
        print ('S')
    q=q//10
    
    if q<p:
        print ('N')
        break