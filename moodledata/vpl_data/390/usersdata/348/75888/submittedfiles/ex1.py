# -*- coding: utf-8 -*-
from __future__ import division
a = float(input( 'digite a: '))
b = float(input( 'digite b: '))
c = float(input( 'digite c: '))
#COMECE A PARTIR DAQUI!
delta = b**2 -4*a*c 
print('%.2f' %delta) 
if delta >= 0:
    print('s') 
else:
    print('SRR') 
