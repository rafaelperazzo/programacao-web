# -*- coding: utf-8 -*-
#ENTRADA
dia1= int(input('Digite o valor para dia 1 (1 a 31): '))
mes1= int(input('Digite o valor para mes 1 (1 a 12): '))
ano1= int(input('Digite o valor para ano 1: '))
dia2= int(input('Digite o valor para dia 2 (1 a 31): '))
mes2= int(input('Digite o valor para mes 2 (1 a 12): '))
ano2= int(input('Digite o valor para ano 2: '))
#PROCESSAMENTO
if dia1 == dia2:
    if mes1==mes2:
        if ano1==ano2:
            print ("IGUAL")
else dia1 > dia2:
    if mes1 > mes2:
        if ano1 > ano2:
            print ('DATA 1')
            


