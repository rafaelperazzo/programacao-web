# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f= float(input('Digite f:'))
l= float(input('Digite l:'))
q= float(input('Digite q:'))
dh= float(input('Digite dh:'))
v= float(input('Digite v:'))
d= (8*f*l*(q*q)/((3.1416)*(9.81*dh)))**(0.5)
rey= (4*q)/3.1416*d*q
k= (0.25)/(log10(0.000002/(3.7*d)+5.74/rey))**2