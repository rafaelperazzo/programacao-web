# -*- coding: utf-8 -*-
#ENTRADA
n=int(input('Valor de n: '))
#PROCESSAMENTO
contador=0
i=2
while (i<n):
    if (n%i)==0:
        print (i)
        contador=contador+1
    i=i+1
if contador>0:
    print