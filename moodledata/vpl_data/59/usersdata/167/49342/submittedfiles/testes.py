# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))

while n>0:
    qa=c//a
    resto=c%a
    qb=resto//b
    if resto!=0 and qb!=0:
        print(qa)
        print(qb)