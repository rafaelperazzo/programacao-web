# -*- coding: utf-8 -*-
p=int(input('digite p:'))
cont=0
for i in range(2,p,1):
    if p%i==0:
        cont=cont+1
        i=i+1
    if cont>0:
        print('não é primo')
        break
    else:
        print('primo')
        break

