# -*- coding: utf-8 -*-
p=int(input('digite o valor de p:'))
q=int(input('digite o valor de q:'))
vtemp=p
i=0
cont=0
while vtemp>0:
    vtemp=vtemp//10
    i=i+1
cont=0
while q>0:
    resto=q%(10**i)
    if resto==p:
        cont=cont+1
    q=q//10
if cont!=0:
    print('sim')
else:
    print('nao')
