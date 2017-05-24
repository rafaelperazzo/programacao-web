# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))

while c>0:
    if a>b:
        qa=c//a
        resto=c%a
        qb=resto//b
        c=c%b
    else:
        qb=c//b
        resto=c%b
        qa=resto//a
        c=c%a
if c!=0:
    print(qa)
    print(qb)
else:
    print('n')