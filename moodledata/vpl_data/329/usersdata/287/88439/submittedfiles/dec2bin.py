# -*- coding: utf-8 -*-
p=int(input('digite o valor 1: '))
q=int(input('digite o valor 2: '))
cont=0
c=0
p1=p
while (p>0):
    cont=cont+1
    p=p//10
while (q>0):
    c=q%(10**cont)
    q=q//10
if c==p1:
    print('S')
else :
    print('N')
   