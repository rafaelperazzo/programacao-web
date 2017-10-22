# -*- coding: utf-8 -*-
import math
v1 = int(input('valor: '))
v2 = int(input('valor: '))
v3 = int(input('valor: '))
v4 = int(input('valor: '))
cont=0
if v1 > v2:
    cont=cont+1
elif v4 > v3:
    cont=cont+1
elif v2 > v1 and v2 > v3:
    cont=cont+1
elif v3 > v2 and v3 > v4: 
    cont=cont+1
elif cont>1:
    print('N')
else:
    print('S')