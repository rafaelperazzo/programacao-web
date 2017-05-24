# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
while c>0:
    if a>b:
        qa=c//a
        c=c%a
        qb=c//b
        c=c%b
    else:
        qb=c//b
        c=c%b
        qa=c//a
        c=c%a
    print(qa)
    print(qb)
