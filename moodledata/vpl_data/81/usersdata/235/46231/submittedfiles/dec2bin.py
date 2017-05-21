# -*- coding: utf-8 -*-
p=int(input('digite o valor de p:'))
q=int(input('digite o valor de q:'))
vtemp=p
i=0
while vtemp>0:
    p=p//10
    i=i+1
while q>0:
    x=p%(10**i)
    q=q//10
    if x==p:
        print('sim)
    else:
        print('nao)
