# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA

a=int(input('digete a carta:'))
b=int(input('digete a carta:'))
c=int(input('digete a carta:'))
d=int(input('digete a carta:'))
e=int(input('digete a carta:'))

a!=b
a!=c
a!=d
a!=e
b!=c
b!=d
b!=e
c!=d
c!=e
n=13

for i in range (1,n+1,1):
    if a>b>c>d>e:
        print('C')
        
    if a<b<c<d<e:
        print('D')

else:

print('N')
