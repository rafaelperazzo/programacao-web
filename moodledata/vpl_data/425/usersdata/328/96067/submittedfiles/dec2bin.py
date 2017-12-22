# -*- coding: utf-8 -*-
p=int(input('Digite o valor de p:'))
q=int(input('Digite o valor de q:'))
p=str(p)
q=str(q)
def sn (a,b):
    return a in b
if sn(p,q):
    print('S')
else:
    print('N')

