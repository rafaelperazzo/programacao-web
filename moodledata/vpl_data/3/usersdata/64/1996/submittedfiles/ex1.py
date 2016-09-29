# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA


a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')


#PROCESSAMENTO/SAÍDA

delta = float(b**2) - (4*a*c)

if delta>=0:
    x1 = (-b + (delta**(1/2.0)))/(2*a)
    x2 = (-b - (delta**(1/2.0)))/(2*a)
    
    print "x1=" + str(x1)
    print "x2=" + str(x2)
    
else:
    print "SRR"