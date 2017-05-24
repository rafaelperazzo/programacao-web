# -*- coding: utf-8 -*-
p=int(input('Digite um número:'))
q=int(input('Digite um número:'))

cont=0
restop=p%10
restoq=q%10

while restoq>0:
    if restop==restoq:
        cont=cont+1
    else:
        restop=p%10
        restoq=q%10
if cont>0:
    print('S')
else:
    print('N')




