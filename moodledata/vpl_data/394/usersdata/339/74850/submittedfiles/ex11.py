# -*- coding: utf-8 -*-


dia1 = int(input('Digite o dia: '))
mes1 = int(input('Digite o mes: '))
ano1 = int(input('Digite o ano: '))

dia2 = int(input('Digite o 2º dia: '))
mes2 = int(input('Digite o 2º mes: '))
ano2 = int(input('Digite o 2º ano: '))

if ano1 > ano2:
    print ('DATA1')
elif ano1 == ano2:
    if mes1 > mes2:
        print ('DATA1')
    elif mes1 == mes2:
        if dia1 > dia2:
            print ('DATA1')
        elif dia1 == dia2:
            print ('IGUAIS')
        else dia1 < dia2:
            print ('DATA2')
    else mes1 < mes2:
        print ('DATA2')
else an1 < ano2:
    print ('DATA2')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
