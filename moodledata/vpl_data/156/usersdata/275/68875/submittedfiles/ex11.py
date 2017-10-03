# -*- coding: utf-8 -*-
dia1= int(input('Digite o dia:'  ))
mes1= int(input('Digite o mes:'  ))
ano1= int(input('Digite o ano:'  ))
dia2= int(input('Digite o dia:'  ))
mes2= int(input('Digite o mes:'  ))
ano2= int(input('Digite o ano:'  ))
if (dia1-mes1-ano1)>(dia2-mes2-ano2):
    print('DATA 2')
if (dia1-mes1-ano1)<(dia2-mes2-ano2):
    print('DATA 2')
if (dia1+mes1+ano1)<(dia2+mes2-ano2):
    print('IGUAIS')


