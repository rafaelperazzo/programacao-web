# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))

cont=0
temp=p

while temp>0:
    cont=cont+1
    p=temp//10

cont2=0
while q>0:
    n=q%(10**cont)
    if n==p:
        cont2=cont2+1
    q=q//10
if cont2>0:
    print('s')
else:
    print('N')