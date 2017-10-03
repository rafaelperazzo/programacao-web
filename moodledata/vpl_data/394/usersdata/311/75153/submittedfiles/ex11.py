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
        print('DATA 1')
    else:
        if (ano2>ano1):
            print('DATA 2')
        else:
            if (mes1>mes2):
                print ('DATA 1')
            else:
                if (mes2>mes1):
                    print('DATA 2')
                else:
                    if (dia1>dia2):
                        print ('DATA 1')
                    else:
                        print ('DATA 2')
                
                
                
                
                
        