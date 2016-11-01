# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
qa=(c//a)
qb=(c%a)//b
if (((c%a)%b)==0):
    print(qa)
    print(qb)
else:
    print('n')
print ('outra saída:')
qb=(c//b)
qa=(((c%b)%a)==0)
    print(qa)
    print(qb)
else:
    print('n')