# -*- coding: utf-8 -*-
numero= int(input('digite um número inteiro que possua 8 algarismos: '))
if 9999999<numero<100000000 :
    X = 0
    while ( numero != 0 ):
        resto= n%10
        numero=((numero-resto)//10
        X = X+resto
    print(X)
else :
    print('NAO SEI')