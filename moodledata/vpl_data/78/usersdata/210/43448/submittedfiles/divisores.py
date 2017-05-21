# -*- coding: utf-8 -*-
import math
E=int(input('digite E:'))
F=int(input('digite F:'))
G=int(input('digite G:'))
for i in range (1,E+4,1):
    if i%F==0 and i%G==0:
        print(i)
    elif i%F==0:
        print(i)
    elif i%G==0:
        print(i)
        





