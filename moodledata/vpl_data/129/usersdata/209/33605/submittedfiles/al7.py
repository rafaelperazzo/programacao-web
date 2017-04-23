# -*- coding: utf-8 -*-
x=int(input('Digite X:'))
contador=0
for i in range (1,x,1):
    if x%i==0:
        contador=contador+i
        print(i)
if contador==x:
    print('PERFEITO')
else:
    print('NÃO PERFEITO')