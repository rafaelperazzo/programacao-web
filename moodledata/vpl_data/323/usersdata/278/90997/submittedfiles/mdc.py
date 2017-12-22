# -*- coding: utf-8 -*-
import math
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
i=1
if n1>n2:
    while (i<=n2):
        if n1%i==0 and n2%i==0:
            mdc=i
        i+=1
    print(mdc)
if n2>n1:
    while (i<=n1):
        if n2%i==0 and n1%i==0:
            mdc=i
        i+=1
    print(mdc)
if n1==n2:
    print(n1)
    
        
    
    
