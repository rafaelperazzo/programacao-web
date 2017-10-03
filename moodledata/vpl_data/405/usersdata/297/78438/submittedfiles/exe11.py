# -*- coding: utf-8 -*-
numero= int(input(''))
if 9999999<numero<100000000 :
    X = 0
    while ( numero != 0 ):
        resto= numero%10
        numero=(numero-resto)//10
        X = X + resto
    print(X)
else :
    print('NAO SEI')