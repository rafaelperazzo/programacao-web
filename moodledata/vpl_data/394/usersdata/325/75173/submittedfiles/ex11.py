# -*- coding: utf-8 -*-

#entrada 
dia1 = int(input('Digite dia 1 :'))
mes1 = int(input('Digite mes 1 :'))
ano1 = int(input('Digite ano 1 :'))
dia2 = int(input('Digite dia 2 :'))
mes2 = int(input('Digite mes 2 :'))
ano2 = int(input('Digite ano 2 :'))

if ano1 == ano2 :
    if mes1 == mes2 :
        if dia1 == dia2 :
            print('iguais')
if ano1 > ano2 :
    print('data 1')
else:
    ano1 == ano2 
    if mes1 > mes2 :
        print('data 1')
    else:
        mes1 == mes2 
        if dia1 > dia2 :
            print('data 1')
if ano1 < ano2 :
    print('data 2')
else:
    ano1 == ano2 
    if mes1 < mes2 :
        print('data 2')
    else:
        mes1 == mes2 
        if dia1 < dia2 :
            print('data 2')
