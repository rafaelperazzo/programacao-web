# -*- coding: utf-8 -*-

dia1 = int(input('Digite o dia1: ' ))
mes1 = int(input('Digite o mes1: ' ))
ano1 = int(input('Digite o ano1: ' ))

DATA1 = (%dia1 %mes1 %ano1)

dia2 = int(input('Digite o dia2: ' ))
mes2 = int(input('Digite o mes2: ' ))
ano2 = int(input('Digite o ano2: ' ))

DATA2 = (%dia2 %mes2 %ano02)

if DATA1 <= DATA2:
    print('DATA1 eh menor que DATA2')