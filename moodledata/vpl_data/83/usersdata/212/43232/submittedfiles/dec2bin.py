# -*- coding: utf-8 -*-
n=int(input('digite um número:'))
binario=0
elevado=0
while(n/2)>0:
    r=n%2
    binario=binario+(r*(10**elevado))
    n=n//2
    elevado=elevado+1
print(binario)

