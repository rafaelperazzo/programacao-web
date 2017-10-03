# -*- coding: utf-8 -*-

n= int(input('Digite o valor de n:'))
contador=0
i=2
while (i<n):
    if (n%i)==0:
        contador=contador+1
        print(i)
    
    i=i+1

if contador>0:
    print('Não Primo')

else:
    print('Primo')
    