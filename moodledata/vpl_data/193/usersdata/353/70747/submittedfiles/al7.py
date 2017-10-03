# -*- coding: utf-8 -*-
#ENTRADA
n=int(input('Valor de n: '))
#PROCESSAMENTO
soma=0
i=1
while (i<n):
    if (n%i)==0:
        print (i)
        soma=soma+i
    i=i+1
if soma==n:
    print ('PERFEITO')
else:
    prin ('NÃO PERFEITO')
