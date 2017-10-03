# -*- coding: utf-8 -*-
dia1= int(input('Digite o Dia:'))
mes1= int(input('Digite o Mes:'))
ano1= int(input('Digite o Ano:'))
dia2= int(input('Digite o Dia:'))
mes2= int(input('Digite o Mes:'))
ano2= int(input('Digite o Ano:'))
if (ano1==ano2) and (mes1==mes2) and (dia1==dia2):
    print ('IGUAIS')
    else:
        if (ano1>ano2):
            print ('Data1')
            else:
                print ('Data2')