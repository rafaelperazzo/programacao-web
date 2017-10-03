# -*- coding: utf-8 -*-
n=int(input('Digite um número: '))
i=1
s=0

while (i<n):
    if(n%i)==0:
        s=s+1
    i=i+1
if s==0:
    print ('PERFEITO')
    
else:
    print ('NÂO PERFEITO')