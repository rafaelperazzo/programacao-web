# -*- coding: utf-8 -*-
from __future__ import division

a = input('a:')
b = input('b:')
c = input('c:')

cont=0
for i in range (0,c+1,a):
    if (c-i)%b==0:
        qa=i//a
        qb=(c-i)//b
        cont=1
if cont==0:
    print('N')
elif cont ==1:
    print(qa)
    print(qb)