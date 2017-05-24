# -*- coding: utf-8 -*-
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
cont=0
temp=a
while temp>0:
    cont=cont+1
    temp=temp//10
cont2=0
while (b>0):
    n=b%(10**cont)
    if n==a:
        cont2=cont2+1
    b=b//10
if cont2>0:
    print('s')
else:
    print('n')

