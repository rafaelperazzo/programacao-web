# -*- coding: utf-8 -*-
import math

a=int(input('digite o valor de a: '))
b=int(input('digite o valor de b: '))
c=int(input('digite o valor de c: '))
#PROCESSAMENTO

if a>b>c:
    maior=c
elif a>c>b:
    maior=b
else:
    maior=a
while True:
    if maior%a==0 and maior%b==0 and maior%c==0:
        print(maior)
        break
    else:
        maior = maior + 1