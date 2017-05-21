# -*- coding: utf-8 -*-

n= int(input('Digite um numero:'))
cont=0
for i in range(2,n,1):
    if n%i==0:
        print(i)
if i%1:
    print('Primo')
else: 
    print('Não Primo')
