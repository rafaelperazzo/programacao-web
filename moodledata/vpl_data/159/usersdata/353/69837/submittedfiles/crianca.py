# -*- coding: utf-8 -*-
#ENTRADA
P1=float(input('Valor de P1: '))
C1=float(input('Valor de C1: '))
P2=float(input('Valor de P2: '))
C2=float(input('Valor de C2: '))
#PROCESSAMENTO
a=P1*C1
b=P2*C2
#SAIDA
if a==b:
    print ('0')
elif a>b:
    print ('-1')
else:
    print ('1')


