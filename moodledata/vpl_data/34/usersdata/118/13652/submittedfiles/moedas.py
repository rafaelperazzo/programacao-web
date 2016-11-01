# -*- coding: utf-8 -*-
from __future__ import division

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

qa = 0
qb = 0


if ((c//a)*a) == c:
    qa = c//a
    qb = 0
    print(qa)
    print(qb)
    else:
        elif ((c//a)*a) != c and (((c%a)//b)*b) == (c%a):
            qa = c//a
        qb = ((c%a)//b)
        print(qa)
        print(qb)
        
elif ((c//b)*b) == c:
    qb = c//b
    qa = 0
    print(qa)
    print(qb)
    else:
         elif ((c//b)*b) != c and (((c%b)//a)*a) == (c%b):
            qb = c//b
            qa = ((c%b)//a)
   
else:
    print('N')


