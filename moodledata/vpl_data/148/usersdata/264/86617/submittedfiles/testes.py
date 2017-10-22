# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a= int(input('Digite o valor:'))
b= float(input('Digite o valor:'))
cont=1
MDC=0

while cont<=a:
   if (a%cont)==0 and (b%cont)==0:
       MDC=cont
       
cont= cont+1
print(MDC)