# -*- coding: utf-8 -*-
dia1 = int(input("Escreva o dia da primeira data: "))
mes1 = int(input("Escreva o mes da primeira data: "))
ano1 = int(input("Escreva o ano da primeira data: "))
dia2 = int(input("Escreva o dia da segunda data: "))
mes2 = int(input("Escreva o mes da segunda data: "))
ano2 = int(input("Escreva o ano da segunda data: "))

r1 = 'DATA 1'
r2 = 'DATA 2'
r3 = 'IGUAIS'

if ano1>ano2:
    print (r1)
elif ano2>ano1:
    print (r2)
elif ano1==ano2 and mes1>mes2:
    print (r1)
elif ano1==ano2 and mes2>mes1:
    print (r2)
elif ano1==ano2 and mes1==mes2 and dia1>dia2:
    print (r1)
elif ano1==ano2 and mes1==mes2 and dia2>dia1:
    print (r2)
elif ano1==ano2 and mes1==mes2 and dia1==dia2:
    print (r3)
    

