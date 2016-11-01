# -*- coding: utf-8 -*-
from __future__ import division
a = input ('Digite o primeiro valor:')
b = input ('Digite o segundo valor:')
c = input ('Digite o terceiro valor :')

quantA = c//a
d = c%a
quantB =d//b
if d%b!=0:
    print ('N')
else:
    print (quantA)
    print (quantB)
