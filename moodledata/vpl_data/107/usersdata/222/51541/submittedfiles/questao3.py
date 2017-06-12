# -*- coding: utf-8 -*-
p=int(input('a:'))
q=int(input('b:'))
cont=0
i=2
while i<a and i<b:
    if a%i==0 and b%i==0:
        cont=cont+1
    i=i+1
if cont==0 and b==a+2:
    print('S')
else:
    print('N')