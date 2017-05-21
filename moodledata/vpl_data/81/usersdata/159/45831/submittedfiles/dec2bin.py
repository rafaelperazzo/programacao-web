# -*- coding: utf-8 -*-
q=int(input('Digite q:'))
p=int(input('Digite p:'))

x=1
i=p
while i>=0:
    if i//10!=0:
        x=x+1
    i=i//10

contador=0
y=n
exp=x
while y>0:
    a=y%(10**exp)
    if a==q:
        contador=contador+1
    y=y//10
    exp=exp+1
if contador!=0:
    print('É subnúmero')
else:
    print('Não é subnúmero')
    
