# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de termos da lista: '))
a=[]
soma_i=0
soma_p=0
for i in range (0,n,1):
    valor=int(input('Digite o termo da lista: '))
    a.append(valor)
    if valor%2 ==0:
        soma_p=soma_p + valor
    

    

