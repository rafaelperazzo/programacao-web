# -*- coding: utf-8 -*-
p=int(input('digite o primeiro numero:'))
q=int(input('digite o segundo numero:'))
contador=0
for i in range (1,p+1,1):
    if p%i!=0:
        contador=contador+1
if contador==2:
    print('S')
else:
    print('N')
