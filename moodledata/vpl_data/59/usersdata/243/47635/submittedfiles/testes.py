# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))

for i in range(1,a+1,1):
    if a%i==0 and b%i==0:
        MDC=i
print(MDC)        