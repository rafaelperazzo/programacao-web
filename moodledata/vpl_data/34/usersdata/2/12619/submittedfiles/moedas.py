# -*- coding: utf-8 -*-
from __future__ import division

a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))


qa = c//a
qb = 0
achou = False
while (qa>0):
    troco = c-qa*a
    if troco%b==0:
        qb = troco//b
        achou = True
        break
    else:
        qa = qa - 1

if not achou:
    while (qb>0):
        troco = c-qb*b
        if troco%a==0:
            qa = troco//a
            achou = True
            break
        else:
            qb = qb - 1

if qa==qb==0:
    print('N')
else:
    print qa
    print qb


