# -*- coding: utf-8 -*-

dia1 = int(input("digite o dia1: "))
mes1 = int(input("digite o mes1: "))
ano1 = int(input("digite o ano1: "))
dia2 = int(input("digite o dia2: "))
mes2 = int(input("digite o mes2: "))
ano2 = int(input("digite o ano2:" ))

if (ano1 == ano2) and (mes1 == mes2) and (dia1 == dia2):
    print ('IGUAIS')
elif (ano1 <= ano2) and (mes1 <= mes2) and (dia1 <= dia2):
    print ('DATA 2')
else:
    print ('DATA 1')
    

    
    
    
