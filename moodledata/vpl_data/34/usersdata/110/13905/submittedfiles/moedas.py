# -*- coding: utf-8 -*-
from __future__ import division
qa=input('Digite quantidade a: ')
qb=input('Digite quantidade b: ')
c=input('Digite o valor: ')
if c%qa==0:
    x=c//qa
    print(x)
    print('0')
elif c%qb==0:
    x=c//qb
    print(x)
    print('0')
else:
    x=c//qb
    resto=c%qb
    y=resto//qa
    if resto%qa==0:
        print(x)
        print(y)
    else:
        print('Não')