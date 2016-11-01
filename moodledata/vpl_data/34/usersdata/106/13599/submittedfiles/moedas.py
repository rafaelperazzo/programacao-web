# -*- coding: utf-8 -*-
from __future__ import division

#entrada
a = input ('Digite um valor para a:')
b = input ('Digite um valor para b:')
c = input ('Digite um valor para c:')

#processamento
if c%a==0:
    d = c //a
    print (d)
elif c%a != 0:
    d = c//a
    e = c%a
    if e%b == 0:
        f = e//b
        print (d)
        print (f)
    else:
        print ('N')