# -*- coding: utf-8 -*-
from __future__ import division
#COMECE A PARTIR DAQUI!
a=float(input('digite o coeficiete a:'))
b=float(input('digite o coeficiente b:'))
c=float(input('digite o coeficiente c:'))
deltaH=((b**2)-(4*a*c))
x1-(((-b)+(deltaH)**(1/2))/2*a)
x2-(((-b)-(deltaH)**(1/2))/2*a)
if deltaH>=0:
    print('%2f'%x1)
    print('%2f'%x2)
else:
    print('SRR')