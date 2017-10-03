# -*- coding: utf-8 -*-
numero= int(input('digite um número inteiro que possua 8 algarismos: '))
a1=int(input('digite o número da dezena de milhão aqui: '))
a2=int(input('digite o número da unidade de milhão aqui: '))
a3=int(input('digite o número da centena de milhar aqui: '))
a4=int(input('digite o número da dezena de milhar aqui: '))
a5=int(input('digite o número da unidade de milhar aqui: '))
a6=int(input('digite o número da centena aqui: '))
a7=int(input('digite o número da dezena aqui: '))
a8=int(input('digite o número da unidade aqui: '))
if 10000000<=numero>=99999999 :
    soma=a1+a2+a3+a4+a5+a6+a7+a8
    print("%.d" %soma)
else :
    print('NAO SEI')