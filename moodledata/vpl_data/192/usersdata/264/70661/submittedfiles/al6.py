# -*- coding: utf-8 -*-
#Entrada:
n= int(input('Digite o valor de n:'))
i= 2
contador= 0
#Processamento e Saída:
while: (i<n):
    if (n%i)==0:
        contador= contador+1
        print (i)
    i= i+1
if contador==0:
    print ('PRIMO')
else:
    print ('NÃO PRIMO')