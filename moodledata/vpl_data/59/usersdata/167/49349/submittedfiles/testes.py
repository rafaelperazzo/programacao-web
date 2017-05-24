# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
qa=c//a

while qa>0:
    resto=c%a
    if resto>=b:
        qb=resto//b
        if qb%b==0:
            print(qa)
            print(qb)
        else:
            print('n')
    