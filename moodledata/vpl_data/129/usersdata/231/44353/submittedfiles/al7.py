# -*- coding: utf-8 -*-
n=int(input('digite valor de n :'))
cont=0
for i in range(1,n,1):
    if n%i==0:
        con=cont+i
if cont==n:
    print('perfeito')
else:
    print('não perfeito')




