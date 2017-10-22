# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n= int(input('Digite o numero:'))
numero=n
soma=0
x=0
cont=0
while n//10>=0:
    x=x+n%10
    soma=soma+x
    n=n//10
    x=soma
    cont=cont+1

print (cont)