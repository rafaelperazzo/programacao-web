# -*- coding: utf-8 -*-

cont=0
while True:
    Número=int(input('Digite seu número inteiro com 8 algarismos: '))
    if (Número/10000000) >= 1:
        Número = Número//10
        cont= cont+1
        print(cont)