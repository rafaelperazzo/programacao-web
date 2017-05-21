# -*- coding: utf-8 -*-
n=int(input('digite o valor de n:'))
contador=0
for i in range(2,n,1):
    if n%i==0:
        print(i)
        contador=contador+1
if contador==0:
    print('PRIMO')
else:
    print(' NÃO PRIMO')
    
    