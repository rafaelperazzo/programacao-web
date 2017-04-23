# -*- coding: utf-8 -*-
a=int(input('esfera1:'))
b=int(input('esfera2:'))
c=int(input('esfera3:'))
d=int(input('esfera4:'))
if a==b+c+d and b+c==d and b==c:
    print('S')
else:
    print('N')
