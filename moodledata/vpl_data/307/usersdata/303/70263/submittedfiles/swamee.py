# -*- coding: utf-8 -*-
import math
f= float(input('Digite f:'))
L= float(input('Digite L:'))
Q= float(input('Digite Q:'))
Deltah= float(input('Digite Delta h:'))
g= 9.81
e= 0.000002
pi= math.pi
D=((8*f*L*(Q**2)/(pi**2)*g*Deltah)**(1/5))
print(D)