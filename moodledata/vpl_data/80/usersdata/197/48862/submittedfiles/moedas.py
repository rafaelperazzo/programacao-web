# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor da moeda a:'))
b=int(input('Digite o valor da moeda b:'))
c=int(input('Digite o valor da cédula c:'))
qa=c//a
resto=c-(qa*a)
qb=resto//2
if qb==0:
    print('N')
else:
    print(qa)
    print(qb)