# -*- coding: utf-8 -*-
a=int(input('Digite um número: '))
s=0
for i in range(1,a,1):
    if a%i==0:
        s=s+1
        print(i)
if s==a:
    print('PERFEITO')
else:
    print('NÃO PERFEITO')
    
        