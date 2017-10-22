# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
for i in range (1000,10000,1) :
    if (i%2!=0) :
        i1= i
        a = i%10
        i = i//10
        b = i%10
        i = i//10
        c = i%10
        i = i//10
        d = i%10
        soma = (d - c + b - a)
        if (soma<0) :
            print(i1)

    
    

