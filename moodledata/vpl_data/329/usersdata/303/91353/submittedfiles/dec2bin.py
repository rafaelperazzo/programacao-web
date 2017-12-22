# -*- coding: utf-8 -*-
p=int(input('digite o valor 1:'))
q=int(input('digite o valor 2:'))
cont=0
c=0
p1=p
while(p>0):
    cont=cont+1
    p=p//10
while (q>0):
    if p1==q%(10**cont):
        c=c+1
    q=q//10
if c>=1:
    print('S')
else:
    print('N')

