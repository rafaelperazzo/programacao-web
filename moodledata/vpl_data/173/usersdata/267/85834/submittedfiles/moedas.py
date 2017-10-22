# -*- coding: utf-8 -*-
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
qa=0
qb=0
while True:
    print ('a = %d, b = %d' %(qa,qb))
    while ((a*qa+b*qb)<c):
        qb=qb+1
        print ('INTERNO: a = %d, b = %d' %(qa,qb))
    if (a*qa+b*qb>=c):
    break
    else:
        qa=qa+1
        qb=0
if (a*qa+b*qb>c):
    print ('N')
else:
    print qa
    print qb