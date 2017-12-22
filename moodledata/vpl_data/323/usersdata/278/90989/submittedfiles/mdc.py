# -*- coding: utf-8 -*-
import math
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
mdc=1
if n1>n2:
    for i in range (2,n2,1):
        resto1=n1%i
        resto2=n2%i
        if resto1==0 and resto2==0:
            mdc=mdc*i
    print(mdc)
if n2>n1:
    for i in range (2,n1,1):
        resto1=n1%i
        resto2=n2%i
        if resto1==0 and resto2==0:
            mdc=mdc*i
    if mdc==1:
        print(mdc)
    else:
        print(mdc)
if n1==n2:
    print(n1)
    
        
    
    
