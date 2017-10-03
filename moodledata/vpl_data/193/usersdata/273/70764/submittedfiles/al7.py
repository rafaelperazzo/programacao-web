# -*- coding: utf-8 -*-
s=0
i=2
n=int(input('Digite o numero de n: '))
while(i<n):
    if(n%i)==0:
        s=s+i
        print(i)
if s==n :
    print('Perfeito')
if s!=n:
    print(' Não perfeito')
