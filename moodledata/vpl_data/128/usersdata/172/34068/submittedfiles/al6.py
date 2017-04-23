# -*- coding: utf-8 -*-
n=int(input('digite um valor: '))
c=0
a=2
while a<n:
    if n%a==0:
        c=c+1
        print(a)
    a=a+1    
if c==0:
    print('PRIMO')
else:
    print('NÃO PRIMO')