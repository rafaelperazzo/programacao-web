# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a= int(input('Digite o valor:'))
b= float(input('Digite o valor:'))
i=1
while i<=a:
   if (a%i)==0 and (b%i)==0:
       MDC=i
    i=i+1
print(MDC)