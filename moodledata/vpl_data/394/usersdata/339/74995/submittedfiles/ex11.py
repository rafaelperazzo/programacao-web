# -*- coding: utf-8 -*-

1<=dia1<=31
1<=dia2<=31

1<=mes1<=12
1<=mes2<=12

dia1 = int(input('Digite o dia: '))
mes1 = int(input('Digite o mes: '))
ano1 = int(input('Digite o ano: '))

dia2 = int(input('Digite o 2º dia: '))
mes2 = int(input('Digite o 2º mes: '))
ano2 = int(input('Digite o 2º ano: '))

if ano1 > ano2:
    print ('DATA 1')
elif ano1 == ano2:
    if mes1 > mes2:
        print ('DATA 1')
    elif mes1 == mes2:
        if dia1 > dia2:
            print ('DATA 1')
        elif dia1 == dia2:
            print ('IGUAIS')
        else  :
            print ('DATA 2')
    else :
        print ('DATA 2')
else :
    print ('DATA 2')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
