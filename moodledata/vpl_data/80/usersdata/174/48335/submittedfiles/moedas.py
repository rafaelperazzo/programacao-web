# -*- coding: utf-8 -*-
from __future__ import division
a = int(input('Digite o valor da moeda a:'))
if a<=0:
    a = int(input('Digite o valor da moeda a:'))
b = int(input('Digite o valor da moeda b:'))
if b<=0:
    b = int(input('Digite o valor da moeda b:'))
c = int(input('Digite o valor da cedula:'))
if c<=0:
    c = int(input('Digite o valor da cedula:'))

qa=0
qb=0

while (qa*a)<c:
    qa=qa+1
if qa*a>c:
    qa=qa-1
qaa=qa
while c%qaa!=(qb*b) and c%qaa!=0:
    if c%qaa<qb*b:
        qaa=qaa-1
    elif c%qaa>=qb*b:
        qb=qb+1
if qaa*a+qb*b==c:
    print qaa
    print qb
else:
    print 'N'