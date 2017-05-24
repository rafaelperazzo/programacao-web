# -*- coding: utf-8 -*-
p=int(input('digite p: '))
q=int(input('digite q: '))
i=0
a=p
while a>0:
    a=a//10
    i=i+1
c=0
while q>0:
    resto=q%(10**i)
    if resto==p:
        c=c+1
    q=q//10
if c!=0:
    print('SIM')
else:
    print('NAO')