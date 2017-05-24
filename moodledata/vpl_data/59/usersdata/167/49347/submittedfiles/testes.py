# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))


while c>0:
    qa=c//a
    resto=c%a
    qb=resto//b
if qa!=0 and qb!=0:
    print(qa)
    print(qb)
else:
    print('n')