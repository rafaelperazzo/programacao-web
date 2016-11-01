# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('de po valor de a: '))
b=int(input('de po valor de b: '))
c=int(input('de po valor de c: '))

na=0
nb=0
cont=0

while na<=c//a:
    nb=(c-(na*a))//b
    if na*a+nb*b==c:
        cont=cont+1
        break
    else
    na=na+1
if cont>0:
    print na
    print nb
else:
    print n