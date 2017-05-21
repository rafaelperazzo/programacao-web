# -*- coding: utf-8 -*-
n=int(input('digite n :'))
cont=0
for i in range(2,n,1):
    if n%2>0:
        cont=cont+1
        print('primo')
    elif n%2==0:
        cont=cont+1
        print('nao primo')