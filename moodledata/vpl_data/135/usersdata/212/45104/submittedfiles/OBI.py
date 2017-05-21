# -*- coding: utf-8 -*-
n=float(input('digite o número de participantes:'))
n=int(n)
p=float(input('digite o valor da pontuação minima a ser alcançado:'))
cont=1
s=0
while cont<=n:
    x=float(input('digite a primeira nota:'))
    x=int(x)
    y=float(input('digite a segunda nota:'))
    y=int(y)
    if (x+y)>=p:
        s=s+1
    cont=cont+1
print(s)