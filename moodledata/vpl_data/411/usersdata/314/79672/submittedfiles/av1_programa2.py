# -*- coding: utf-8 -*-
n=float(input('Digite o valor do produto: '))
opçao=int(input('digite um numero de 1 a 4: '))
opçao1=n-(n*(15/100))
opçao2=n-(n*(10/100))
opçao3=n
opçao4=n+(n*(10/100))
if opçao1 :
    print('{:.2f}'.format(opçao1))
elif opçao2:
    print('{:.2f}'.format(opçao2))
elif opçao3:
    print('{:.2f}'.format(opçao3))
elif opçao4:
    print('{:.2f}'.format(opçao4))
    