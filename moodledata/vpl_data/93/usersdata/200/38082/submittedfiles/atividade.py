# -*- coding: utf-8 -*-
import math
n=int(input('digite n'))
cont=1
while cont<=n:
    x=int(input('digite x:'))
    y=int(input('dogite y:'))
    if x>=0 and y>=0 and ((x**2)+(y**2))<=1:
        print('SIM')
    else:
        print('NAO')
    cont=cont+1


