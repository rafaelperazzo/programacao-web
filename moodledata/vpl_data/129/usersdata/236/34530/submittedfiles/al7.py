# -*- coding: utf-8 -*-
n= int(input('Digite o número:'))
contador=0
for i in range (1,n,1):
    a=n%i
    if a==0:
        print(i)
    contador=contador+i
if (contador-n) == n:
    print ('perfeito')
else:
    print('não perfeito')
