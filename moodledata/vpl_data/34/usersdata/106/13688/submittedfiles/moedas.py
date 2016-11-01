# -*- coding: utf-8 -*-
from __future__ import division

#entrada
a = input ('Digite um valor para a:')
b = input ('Digite um valor para b:')
c = input ('Digite um valor para c:')

#processamento
if c%a==0:
    qa = c //a
    qb = 0
    print (qa)
    print (qb)
elif c%a != 0:
    qa = c//a
    d = c%a
    if d%b == 0:
        qb = d//b
        print (qa)
        print (qb)
    else:
        print ('N')