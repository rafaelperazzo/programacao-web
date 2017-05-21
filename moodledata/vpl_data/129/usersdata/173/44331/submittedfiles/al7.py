# -*- coding: utf-8 -*-
n=int(input('Digite um número: '))
s=0
for i in range(1,n,1):
    if(n%i==0):
        print(i)
        s=s+1
if(s==0):
    print('PERFEITO')
else:
    print('NÃO PERFEITO')