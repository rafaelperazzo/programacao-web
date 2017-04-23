# -*- coding: utf-8 -*-
import math
a=float(input('Valor de A:'))
b=float(input('Valor de B:'))
c=float(input('Valor de C:'))
d=float(input('Valor de D:'))
cont=0
if a>b:
    cont=cont+1
elif b>a and c>d:
    cont=cont+1
elif d>c:
    cont=cont+1
elif cont==1:
    print('S')
else:
    print('N')
