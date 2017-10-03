# -*- coding: utf-8 -*-
#Entrada:
dia1= int(input('Digite o dia1:'))
mês1= int(input('Digite o mês1:'))
ano1= int(input('Digite o ano1:'))
dia2= int(input('Digite o dia2:'))
mês2= int(input('Digite o mês2:'))
ano2= imt(input('Digite o ano2:'))
#Processamento e Saída:
if (ano1>ano2):
    print ('DATA 1')
if (ano2>ano1):
    print ('DATA 2')
if (ano1==ano2) and (mês1>mês2):
    print ('DATA 1')
if (ano1==ano2) and (mês2>mês1):
    print ('DATA 2')
if (ano1==ano2) and (mês1==mês2) and (dia1>dia2):
    print ('DATA 1')
if (ano1==ano2) and (mês1==mês2) and (dia2>dia1):
    print ('DATA 2')
 if(ano1==ano2) and (mês1==mês2) and (dia1==dia2):
    print ('IGUAIS')
   