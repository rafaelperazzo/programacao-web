# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!

Delta = (b**2) - (4*a*c)

if Delta >= 0:
    x1 = (- b + ((Delta)**0.5))/2*a
    x2 = (- b - ((Delta)**0.5))/2*a

print (' o valor de x1 eh: %.2f' %x1) 
print (' o valor de x2 eh: %.2f' %x2)

else:
    print ( 'SRR: Sem Raízes Reais' )
    