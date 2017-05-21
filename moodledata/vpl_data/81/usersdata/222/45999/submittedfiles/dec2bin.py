# -*- coding: utf-8 -*-
q=int(input('q:'))
p=int(input('p:'))
i=0
temp=p
while temp>0:
    temp=temp//10
    i=i+1
cont=0
while p>0:
    resto=p%(10**i)
    if resto==q:
        cont=cont+1
    p=p//10
if cont!=0:
    print('S')
else:
    print('N')

