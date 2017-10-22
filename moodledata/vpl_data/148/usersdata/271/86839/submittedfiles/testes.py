# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
for i in range (1000,10000,1) :
    a = i%10
    i = i//10
    b = i%10
    i = i//10
    c = i%10
    i = i//10
    d = i%10
    soma = (d - c + b - a)
    print(soma)

    
    

