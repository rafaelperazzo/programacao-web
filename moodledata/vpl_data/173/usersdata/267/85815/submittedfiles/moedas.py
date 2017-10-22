# -*- coding: utf-8 -*-
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
qa=0
qb=0
while (a*qa+b*qb<c):
    if (a*qa>=c):
        break
    print ('a = %d, b = %d' %(qa,qb))
    while ((a*qa+b*qb)<c):
        qb=qb+1
        print ('INTERNO: a = %d, b = %d' %(qa,qb))
    qb=0
    qa=qa+1
if (a*qa+b*qb>c):
    print ('N')
else:
    print qa
    print qb