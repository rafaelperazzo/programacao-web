# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
if a>b>c:
    maior=a
    else b>a>c:
        maior=b
        else: c>a>b:
            maior=c
cont=0
mmc=maior
while cont==0:
    if(mmc%a==0) and (mmc%b==0) and (mmc%c==0):
        cont=cont+1
    else:
            mmc=mmc+1
            print ('mmc')
