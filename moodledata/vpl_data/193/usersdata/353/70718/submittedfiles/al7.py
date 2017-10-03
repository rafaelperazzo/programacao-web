# -*- coding: utf-8 -*-
#ENTRADA
n=int(input('Valor de n: '))
#PROCESSAMENTO
soma=0
i=1
while (i<n):
    if (n%i)==0:
        print (i)
        soma=soma+1
    i=i+1

