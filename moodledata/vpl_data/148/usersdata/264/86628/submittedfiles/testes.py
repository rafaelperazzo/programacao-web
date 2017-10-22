# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n= int(input('Digite o número de temos:'))
numerador=1
denominador=1
soma=0
i=1
while (i<=n):
    if (i%2)==0:
        soma= soma- (i)/(i*i)
    else:
        soma= soma+ (i)/(i*i)
    print (soma)