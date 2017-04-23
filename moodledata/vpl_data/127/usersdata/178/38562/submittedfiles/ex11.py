# -*- coding: utf-8 -*-
dia1=int(input('Digite o dia 1: '))
mes1=int(input('Digite o mes 1: '))
ano1=int(input('Digite o ano 1: '))

dia2=int(input('Digite o dia 1: '))
mes2=int(input('Digite o mes 2: '))
ano2=int(input('Digite o ano 2: '))

if ano1>ano2:
    print('Data 1')
    
elif ano1<2:
    print('Data 2')
    
else:
    if mes1>mes2:
        print ('Data 1')
        
    elif mes1<mes2:
        print('Data2')
            
    else:
        if dia1>dia2:
            print('Data 1')
                
        elif dia1>dia2:
            print('Data 2')
                
        else:
            print('Iguais')
                
            
        


