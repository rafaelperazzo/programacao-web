# -*- coding: utf-8 -*-
import math
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
if n1>n2:
    resto = n1%n2
    while (resto>0):
        resto_ = n2/resto
        if resto_==0:
            print(resto)
            break
        else:
            n2=resto
            resto=resto_
            continue
    if resto==0:
        print(n2)
if n2>n1:
    resto = n2%n1
    while (resto>0):
        resto_ = n1/resto
        if resto_==0:
            print(resto)
            break
        else:
            n1=resto
            resto=resto_
            continue
    if resto==0:
        print(n1) 
if n1==n2:
    print(n1)
            
    
    
