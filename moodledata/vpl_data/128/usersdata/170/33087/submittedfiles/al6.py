# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n:'))
CONTADOR=0
i=2
while i<n:
    if n%i==0:
        CONTADOR=CONTADOR+1
        print(n/i)
        i=i+1
if CONTADOR==0:
    print('PRIMO')
else:
    print('NÃO PRIMO')