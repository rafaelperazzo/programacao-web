# -*- coding: utf-8 -*-
p=int(input('digite o valor de p:'))
q=int(input('digite o valor de q:'))
vtemp=p
i=0
cont=0
while vtemp>0:
    p=p//10
    i=i+1
cont=0
while q>0:
    resto=p%(10**i)
    q=q//10
    if resto==p:
        cont=cont+1
    if cont!=0:
        print('sim')
    else:
        print('nao')
