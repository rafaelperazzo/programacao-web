# -*- coding: utf-8 -*-
n=int(input('digite um número:'))
i=0
for cont in range(1,n,1):
    if n%i==0:
        print(cont)
        i=i+i
if se i==n:
    print('perfeito')
else:
    print('não perfeito') 
