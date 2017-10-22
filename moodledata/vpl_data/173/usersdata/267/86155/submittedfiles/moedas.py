# -*- coding: utf-8 -*-
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
qa=0
qb=0
while True:
    #print ('a = %d, b = %d' %(qa,qb))
    while ((a*qa+b*qb)<c):
        qb=qb+1
        soma=(qa*a+qb*b)
        print ('INTERNO: a = %d, b = %d, soma = %d' %(qa,qb,soma))
        if (a*qa+b*qb>=c):
            break
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