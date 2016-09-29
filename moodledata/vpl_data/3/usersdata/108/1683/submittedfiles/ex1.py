# -*- coding: utf-8 -*-
from __future__ import division

# -*- coding: utf-8 -*-
from __future__ import division

a = input ('Digite o coeficiente angular da equação:')
b = input ('Digite o coeficiente linear da equação:')
c = input ('Digite o termo independente:')

delta = (b**2)-(4*a*c)

if (delta>0):
    x1 = (-b+(delta**0.5))/(2*a)
    x2 = (-b-(delta**0.5))/(2*a)
    
    print (x1)
    print (x2)
    
elif (delta==0):
    x = (-b+(delta**0.5))/(2*a)
    
    print (x)

else:
    print ('A equação não possui raízes reais')