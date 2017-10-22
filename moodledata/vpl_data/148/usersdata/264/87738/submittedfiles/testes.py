# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n= int(input('Digite o numero:'))
n=numero
soma=0
x=0
cont=0
while n//10>=0:
    x=x+n%10
    soma=soma+x
    n//10=n
    cont=cont+1

if cont<8:
    print ('NAO SEI')
if cont==8:
    print (soma)