# -*- coding: utf-8 -*-
p=int(input('Digite um numero p:'))
q=int(input('Digite um numero q:'))
contador=0
i=2
while i<(p) and (q):
    if p%i==0 and q%i==0:
        contador=contador+1
        if q==p+2:
            print('S')
else:
    print('N')
   
