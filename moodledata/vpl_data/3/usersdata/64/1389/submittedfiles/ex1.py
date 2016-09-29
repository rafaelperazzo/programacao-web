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
    
    print "O valor de x1 é: " + str(x1)
    print "O valor de x2 é: " + str(x2)
    
else:
    print "SRR"