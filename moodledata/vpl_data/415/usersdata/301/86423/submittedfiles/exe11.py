# -*- coding: utf-8 -*-
n = int(input('digite um numero inteiro de oito algarismos: '))
if n>=100000000 or n <10000000:
    print('NAO SEI')
else:
    s=0
    i=1000000
    while (n//1):
        a=n//1
        s=s+a
        n=n%1
        i=i//10
    print('%.d'%(s))
        