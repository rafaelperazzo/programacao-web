# -*- coding: utf-8 -*-
import math

a=int(input(' Digite o valor a: '))
b=int(input(' Digite o valor b: '))
c=int(input(' Digite o valor c: '))
d=int(input(' Digite o valor d: '))

if ((a>b) and ( b>=c) and (c>=d)) or ((a>b) and (b==c==d)):
    print('S')
elif ((d>c) and (c>=b) and (b>=a)) or ((d>c) and (b==c==a)):
    print('S')
elif (a<b) and (b>c) and (c>=d) or ((b>c) and (b>a) and (d==c==a)):
    print('S')
elif (c>d) and (c>b) and (b>=a) or ((b<c) and (c>d) and (d==a==b)):
    print('S')
else:
    print('N')