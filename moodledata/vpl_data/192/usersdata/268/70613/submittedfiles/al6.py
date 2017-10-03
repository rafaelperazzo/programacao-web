# -*- coding: utf-8 -*-
n=int(input('Digite o número'))
i=2
CONT=0

while (i<n):
    if (n%i)==0:
        CONT= CONT+ 1
        print (i)
    i=i+1
if (CONT!=0):
    print('NÃO É PRIMO')