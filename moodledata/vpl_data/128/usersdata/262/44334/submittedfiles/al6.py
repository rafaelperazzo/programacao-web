# -*- coding: utf-8 -*-
n=(int(input('digite o valor de n:'))
cont=0
for i in range(2,n,1):
    if n%i==0:
        cont=cont+1
        print(i)
if cont==0:
    print('PRIMO')
else :
    print('NÃO PRIMO')
