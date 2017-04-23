# -*- coding: utf-8 -*-
n=int(input('digite um número:'))
i=0
for cont in range(2,n,1):
    if n%cont==0:
        print(cont)
        i=i+i
if i==n:
    print('perfeito')
else:
    print('não perfeito') 
