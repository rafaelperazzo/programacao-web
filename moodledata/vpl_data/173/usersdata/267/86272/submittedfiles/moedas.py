# -*- coding: utf-8 -*-
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
qa=-1
qb=0
soma=(qa*a+qb*b)
while (soma<c):
    qa=qa+1
    qb=0
    while True:
        qb=qb+1
        print ('INTERNO: a = %d, b = %d, soma = %d' %(qa,qb,soma))
        if (soma>=c):
            break
        
if (soma>c):
    print ('N')
else:
    print qa
    print qb