# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos:'))
a=int(input('Digite um número:'))
b=int(input('Digite um número:'))
i=1
while (n>0):
    if (i%a==0) or (i%b==0):
        print(i)
        n=n-1
        i=i+1
    else:
        i=i+1

for i in range(1,100000000,1):
    if n>0:
        if (i%a==0) or (i%b==0):
            print(i)
            n=n-1
            

