# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a1=int(input('Digite a aposta: '))
a2=int(input('Digite a aposta: '))
a3=int(input('Digite a aposta: '))
a4=int(input('Digite a aposta: '))
a5=int(input('Digite a aposta: '))
a6=int(input('Digite a aposta: '))
cont=0
for i in range (0,6,1):
    sort=int(input('Digite o número sorteado: '))
    if sort==a1 or sort==a2 or sort==a3 or sort==a4 or sort==a5 or sort==a6:
        cont=cont+1
if cont==3:
    print('terno')
if cont==4:
    print ('quadra')
if cont==5:
    print ('quina')
if cont==6:
    print ('sena')
if cont<3:
    print ('azar')