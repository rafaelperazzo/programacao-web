# -*- coding: utf-8 -*-
#Entrada:
n= int(input('Digite o valor de n:'))
i=1
contador=0
#Processamento e Saída:
while (i<n):
    if (n%i)==0:
        contador= contador+i
        print (i)
    i= i+1
if (contador==n):
    print ('PERFEITO')
else:
    print ('NÃO PERFEITO')