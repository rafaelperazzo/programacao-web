# -*- coding: utf-8 -*-
p=int(input('digite o valor mínimo para ser convidado:'))
x1=int(input('digite a primeira pontuação:'))
y1=int(input('digite a segunda pontuação:'))
x2=int(input('digite a primeira pontuação:'))
y2=int(input('digite a segunda pontuação:'))
x3=int(input('digite a primeira pontuação:'))
y3=int(input('digite a segunda pontuação:'))
x4=int(input('digite a primeira pontuação:'))
y4=int(input('digite a segunda pontuação:'))
jogador1=x1+y1
jogador2=x2+y2
jogador3=x3+y3
jogador4=x4+y4
soma=0
if jogador1>=p:
    soma=soma+1
if jogador2>=p:
    soma=soma+1
if jogador3>=p:
    soma=soma+1
if jogador4>=p:
    soma=soma+1
print(soma)