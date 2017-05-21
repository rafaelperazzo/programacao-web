# -*- coding: utf-8 -*-
import math
n=float(input('digite o valor do número de multiplos:'))
n=int(n)
a=float(input('digite o valor do primeiro número:'))
a=int(a)
b=float(input('digite o valor do segundo número:'))
b=int(b)
if a<0 or b<0 or (a<0 and b<0) or n<0:
    print('erro.este programa só adimite números positivos')
ia=1
ib=1
ma=0
mb=0
cont=0
while cont<n:
    ma=ia*a
    mb=ib*b
    if ma<mb:
        print(ma)
        ia=ia+1
    elif mb<ma:
        print(mb)
        ib=ib+1
    else:
        print(mb)
        ia=ia+1
        ib=ib+1
    cont=cont+1    
    