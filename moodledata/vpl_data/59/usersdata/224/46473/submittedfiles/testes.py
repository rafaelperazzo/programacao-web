# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
a=int(input('Digite a: '))
b=int(input('Digite b: '))
i=1
while i<n:
    if a*i!=b*i:
        print('%d'%(a*i))
        print('%d'%(b*i))
    i=i+1
    else:
        print('%d'%(a*i))
    i+i+2
