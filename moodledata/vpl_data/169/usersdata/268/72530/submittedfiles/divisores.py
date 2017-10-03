# -*- coding: utf-8 -*-
import math

n=int(input('Digite a quantidade de multiplos: '))
a=int(input('Digite o numero a : '))
b=int(input('DIgite o numero b : '))
i=1
if (a<b):
    while(i<=n/2):
        multiploa=a*i
        print(multiploa)
        multiplob=b*i
        print(multiplob)
        i= i + 1
else:
     while(i<=n/2):
        multiplob=b*i
        print(multiplob)
        multiplob=a*i
        print(multiploa)
        i= i + 1
    