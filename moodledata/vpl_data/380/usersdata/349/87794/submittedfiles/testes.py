# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

dia1 = int(input("digite o dia1: "))
mes1 = int(input("digite o mes1: "))
anus1 = int(input("digite o anus1: "))
dia2 = int(input("digite o dia2: "))
mes2 = int(input("digite o mes2: "))
anus2 = int(input("digite o anus2: "))

if (anus1 == anus2) and (mes1 ==mes2) and (dia1 == dia2):
    print ('IGUAIS')
    
elif (anus1 <= anus2) and (mes1 <= mes2) and (dia1 <= dia2):
    print ('DATA2')
    
else: 
    print ('meus ovo')