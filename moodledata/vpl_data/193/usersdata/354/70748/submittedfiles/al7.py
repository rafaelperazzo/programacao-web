# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n: '))

i=1
s=0

while (i<n):
    if (n%i)==0:
        s=s+i
        print(i)
    i=i+1
if s==0:
    print('PERFEITO')
else: 
    print('NÃO PERFEITO')
    