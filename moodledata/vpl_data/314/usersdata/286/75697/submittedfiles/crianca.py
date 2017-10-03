# -*- coding: utf-8 -*-
p1 = float ( input('DIGITE O PESO DA CRIANÇA 1: '))
c1 = float ( input('DIGITE O COMPRIMENTO 1: '))
p2 = float ( input('DIGITE O PESO DA CRIANÇA 2: '))
c2 = float ( input('DIGITE O COMPRIMENTO 2: '))

if p1*c1==p2*c2:
    print(" '0' ")
elif p1 * c1 > p2 * c2 :
    print(" '-1' ")
else:
    print(" '1' ")

