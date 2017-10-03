# -*- coding: utf-8 -*-
#ENTRADA
n1 = float(input('Digite o 1 número: ))
n2 = float(input('Digite o 2 número: ))
n3 = float(input('Digite o 3 número: ))
#PROCESSAMENTO
if(n1>n2):
   aux=n1
    n1=n2
    n2=aux
if(n1>n3):
    aux=n1
    n1=n3
    n3=aux
if(n2>n3):
    aux=n2
    n2=n3
    n3=aux
print(n1)
print(n2)
print(n3)
