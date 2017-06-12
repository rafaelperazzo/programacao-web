# -*- coding: utf-8 -*-
p=int(input('digite o valor p:'))
cont=0
i=2
while i<p:
    if p%i==0:
        cont=cont+1
    i=i+1    
if cont==0:
    print('s')
else:
    print('n')
