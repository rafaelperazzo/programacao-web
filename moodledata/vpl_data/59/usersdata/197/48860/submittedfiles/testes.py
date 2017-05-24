# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c'))
qa=c//a
resto=c-qa*a
qb=resto//2
if qb==0:
    print('N')
else:
    print(qa)
    print(qb)