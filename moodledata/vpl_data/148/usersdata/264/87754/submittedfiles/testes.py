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
    cont=cont+1
    n=n//10
    soma=soma
    

if cont!=8:
    print ('NAO SEI')
if cont==8:
    print (soma)