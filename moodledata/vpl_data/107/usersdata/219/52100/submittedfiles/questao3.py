# -*- coding: utf-8 -*-
p=int(input('Digite um numero p:'))
q=int(input('Digite um numero q:'))
i=2
contador=0
while i<=((p) and (q)):
    if (p%i)==0 and (q%i)==0:
        contador=contador+1
        break
    if (p==p+2):
        print('S')
    else:
        print('N')
        
