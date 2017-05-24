# -*- coding: utf-8 -*-

a=int(input('digite a:'))
b=int(input('digite b:'))


termo=a
cont=0
cont1=0

while termo>0:
    termo=termo//10
    cont=cont+1

while b>0:
    p=b%(10**cont)
    if p==a:
        cont1=cont1+1
    b=b//10
if cont1>0:
    print ('s')
else:
    print('n')
