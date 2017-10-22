# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n= int(input('Digite o número de temos:'))
numerador=1
denominador=1
soma=0

while numerador<n:
    if numerador%2==0:
        soma=soma-(numerador)/(denominador**2)
    else:
        soma=soma+(numerador)/(denominador**2)
numerador= numerador+1
denominador= (denominador+1)**2

print ('%.5f' %soma)