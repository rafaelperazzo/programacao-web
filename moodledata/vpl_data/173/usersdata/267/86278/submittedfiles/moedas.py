# -*- coding: utf-8 -*-
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
qa=0
qb=0
soma=0
while (soma<c):
    qb=0
    while soma<c:
        qb=qb+1
        soma=(qa*a+qb*b)
        print ('INTERNO: a = %d, b = %d, soma = %d' %(qa,qb,soma))
    if (soma==c):
        break
    else:
        qa=qa+1
if (soma>c):
    print ('N')
else:
    print qa
    print qb