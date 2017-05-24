# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
x=1
i=p
while i>0:
    if i//10!=0:
        x=x+1
    i=i//10
contador=0
y=q
exp=x
while y>0:
    a=y%(10**exp)
    if a==p:
        contador=contador+1
    y=y//10
if contador!=0:
    print('S')
else:
    print('N')