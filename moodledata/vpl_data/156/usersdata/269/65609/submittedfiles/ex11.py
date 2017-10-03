# -*- coding: utf-8 -*-
dia1=int(input('digite dia 1: '))
mes1=int(input('digite mes 1: '))
ano1=int(input('digite ano 1: '))
dia2=int(input('digite dia 2: '))
mes2=int(input('digite mes 2: '))
ano2=int(input('digite ano 2: '))

if ano2>ano1:
    print('DATA 2')
if ano2==ano1:
    print('IGUAIS')
if ano2<ano1:
    print('DATA 1')

if ano1==ano2 and mes1>mes2:
    print('DATA 1')
if ano1==ano2 and mes1==mes2:
    print('IGUAIS')
if ano1==ano2 and mes1<mes2:
    print('DATA 2')
    
if ano1==ano2 and mes1==mes2 and dia1>dia2:
    print('DATA 1')
    

if ano1==ano2 and mes1==mes2 and dia1==dia2:
    print('IGUAIS')

if ano1==ano2 and mes1==mes2 and dia1<dia2:
    print('DATA 2')