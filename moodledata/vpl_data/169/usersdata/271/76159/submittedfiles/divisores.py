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
while (i<=n) :
    a1 = (a1*a)
    b1 = (b1*b)
    if (a>b) and (b%a!=0) :
        if (a1<b1) and (a1>b1/2) :
            print(a1)
            print(b1)
    if (b>a) and (a%b!=0) :
        if (b1<a1) and (b1>a1/2) :
            print(b1)
            print(a1)
    if (a>b) and (b%a==0) :
        if (a1<b1) and (a1==b1/2) :
            print(a1) or print(b1)
            print(a1) or print(b1)
    if (a<b) and (b%a==0) :
        if(b1<a1) and (b1==a1/2) :
            print(b1) or print(a1)
            print(b1) or print(a1)
    i = i+1
            
            


