# -*- coding: utf-8 -*-
#PROGRAMA
P=float(input('Digite o valor da etiqueta: '))
x=int(input('Escolha a forma de pagamento: '))
if x==1 :
    y=(P/100)*85
    print('%.2f' %y)
if x==2 :
    y=(P/100)*90
    print('%.2f' %y)
if x==3 :
    y=P
    print('%.2f' %y)
if x==4 :
    y=(P/100)*110
    print('%.2f' %y)