# -*- coding: utf-8 -*-
p1=float(input('peso do lado esquerdo:'))
p2=float(input('peso do lado direito:'))
c1=float(input('comprimento do lado esquerdo:'))
c2=float(input('conprimento do lado direito:'))
e=p1*c1
d=p2*c2
if e>d:
    print('-1')
elif d>e:
    print('1')
else:
    print('0')
    


