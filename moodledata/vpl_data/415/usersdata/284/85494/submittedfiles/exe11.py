# -*- coding: utf-8 -*-
n=int(input('digite um número de 8 algarismos: '))
while( 10000000<=n<=99999999):
    if(n//10**8>=0):
        print(n//10**8)
        break