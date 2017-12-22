# -*- coding: utf-8 -*-
n= int(input('Digite o valor de n:'))
m= int(input('Digite o valor de m:'))
t=0
cont=0

for i in range (0,n-1,1):
    x= int(input('Digite o valor de x:'))
    t=x-t
    if t<=m:
        cont= cont+0
    if t>m:
        cont= cont+1
if con==0:
    print('S')
else:
    print('N')