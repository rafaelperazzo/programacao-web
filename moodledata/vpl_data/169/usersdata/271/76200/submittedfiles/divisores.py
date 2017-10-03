# -*- coding: utf-8 -*-
import math
#ENTRADA
n = int(input('Digite o numero de multiplos : '))
a = int(input('Digite o valor de a : '))
b = int(input('Digite o valor de b : '))
a1 = 1
b1 = 1
i = 1
#PROCESSAMENTO
while (i<=n/2) :
    a1 = (a*2)
    b1 = (b*2)
    if (a>b) :
        print(b)
        print(a)
    elif (b>a) :
        print(a)
        print(b)
    if (a1>b1) :
        print(b1)
        print(a1)
    elif (a1<b1) :
        print(a1)
        print(b1)
    a = a+a
    b = b+b
    i = i+1
            
            


