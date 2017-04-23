# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n:'))
i=2
while i<n:
    if n%i==0:
        print(i)
        contador=contador+1
    i=i+1  
if contador==0:
    print('PRIMO')
else:
    print('NÃO PRIMO')