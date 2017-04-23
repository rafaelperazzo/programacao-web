# -*- coding: utf-8 -*-
a=int(input('Digite a:'))
contador=0
for i in range(2,a,1):
    if n%i==0:
        contador=contador+1
        print(i)
    i=i+1
if contador==0:
    print('PRIMO')
else:
    print('NÃO PRIMO')

    
    
