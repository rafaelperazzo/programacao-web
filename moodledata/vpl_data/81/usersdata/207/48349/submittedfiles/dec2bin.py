# -*- coding: utf-8 -*-
v=int(input('escreva o valor de v:'))
l=int(input('escreva o valor de l:'))
cont=0
temp=v
while temp>0:
    cont=cont+1
    temp=temp//10
cont2=0
while (l>0):
    n=l%(10**cont)
    if n==v:
        cont2=cont2+1
    l=l//10
if cont2>0:
    print('s')
else:
    print('n')
