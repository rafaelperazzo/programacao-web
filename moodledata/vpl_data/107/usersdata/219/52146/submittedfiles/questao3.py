# -*- coding: utf-8 -*-
q=int(input('Digite um numero q:'))
p=int(input('Digite um numero p:'))
i=2
contadorq=0
contadorp=0
while i<q:
    if (q%i)==0:
        contador=contador+1
while i<p:
    if (p%i)==0:
        contador=contador+1
        if (p==q+2):
            print('S')
        else:
            print('N')
        
