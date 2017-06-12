# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
contador=0
i=2
while i<p:
    if p%i==0:
        contador=contador+1
    i=i+1
if contador==0:
    print('S')
else:
    print('N')
    

    


