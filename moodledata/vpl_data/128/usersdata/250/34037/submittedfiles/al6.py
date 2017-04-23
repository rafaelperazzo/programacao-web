# -*- coding: utf-8 -*-
n=int(input('digite um valor:'))
i=1
contador=0
while i<(n-1):
    if (n%i==0):
        contador=contador+1
    i=i+1
if contador>0:
    print('%d'%contador)
    print('n e primo!')
else:
    print('n nao e primo!')
