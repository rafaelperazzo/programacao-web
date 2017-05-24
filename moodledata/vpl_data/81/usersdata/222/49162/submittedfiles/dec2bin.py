# -*- coding: utf-8 -*-
p=int(input('p:'))
q=int(input('q:'))
x=1
i=p
while i>0:
    if i//10!=0:
        x=x+1
    i=i//10
cont=0
y=p
exp=x
while y>0:
    a=y%(10**exp)
    if a==p:
        cont=cont+1
    y=y//10
if cont!=0:
    print('S')
else:
    print('N')

