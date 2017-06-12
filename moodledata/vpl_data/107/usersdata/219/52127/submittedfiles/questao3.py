# -*- coding: utf-8 -*-
q=int(input('Digite um numero q:'))
p=int(input('Digite um numero p:'))
i=2
contador=0
while i<=((p) and (q)):
    if (p%i)==0 and (q%i)==0:
        contador=contador+1
        if (p==q+2):
            print('S')
        else:
            print('N')
        
