# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
cont1=0
cont2=0
for i in range(2,p,1):
    if p%i==0:
        cont1=cont1+1
for i in range(2,q,1):
    if q%i==0:
        cont2=cont2+1
if cont1==0 and cont2==0:
    d=p+2
    if q==d:
        print('S')
    else:
        print('N')
else:
    print('N')





