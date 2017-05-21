# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n:'))
cont=0
for i in range(2,n,1):
    if n%1==0:
        print(i)
        cont=cont+1
if cont==0:
    print('primo')
else:
    print('não primo')