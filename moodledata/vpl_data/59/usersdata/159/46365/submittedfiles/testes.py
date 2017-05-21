# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Número de pessoas:'))
m=int(input('Número de mulheres:'))
h=int(input('Número de homens:'))

maiormulher=0
contmulheres=0
for i in range (1,m+1,1):
    am=float(input('Altura:'))
    contmulheres=contmulheres+am
    if am>=maiormulher:
        maiormulher=am
    else:
        menormulher=am
    print('A maior mulher tem: %.2f' %maiormulher)
    print('A menor mulher tem: %.2f' %menormulher)

maiorhomem=0
conthomem=0
for k in range (1,h+1,1):
    ah=float(input('Altura:'))
    conthomem=conthomem+ah
    if ah>=maiorhomem:
        maiorhomem=ah
    else:
        menorhomem=ah
    print('O maior homem tem: %.2f' %maiorhomem)
    print('O menor homem tem: %.2f' %menorhomem)
    
mediamulheres=contmulheres/m
mediahomens=conthomem/h

print('A média de altura feminina: %.2f' %mediamulheres)
print('A média de altura masculina: %.2f' %mediahomens)