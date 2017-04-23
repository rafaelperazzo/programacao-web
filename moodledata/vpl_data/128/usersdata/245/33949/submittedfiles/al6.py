# -*- coding: utf-8 -*-
n=int(input('Digite um numero inteiro:'))
contador=0
i=2
while i<n:
    if n%i==0:
        contador=contador+1
        print(i)
    i=i+1
if contador!=0:
    print('Não é Primo')
else:
    print('Primo')