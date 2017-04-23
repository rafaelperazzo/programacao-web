# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n:'))
CONTADOR=0
for i in range (2,n,1):
    if n%i==0:
        CONTADOR=CONTADOR+1
        print(i)
    i=i+1
if CONTADOR==0:
    print('PRIMO')
else:
    print('NÃO PRIMO')