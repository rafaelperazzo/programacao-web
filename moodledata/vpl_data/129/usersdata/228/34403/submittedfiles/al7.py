# -*- coding: utf-8 -*-
n=int(input('digite um valor:'))
contador=0
i=1
while i<n:
    if n%i==0:
        contador=contador+1
    i=i+1    
if contador==n:
    print('PERFEITO')
else:
    print('NÃO PERFEITO')

        
        