# -*- coding: utf-8 -*-

def impar(x):
    if x%2==1:
        return(True)
    else:
        return(False)
for i in range(1000,10000,1) :
    soma = 0
    cont = 1
    if (i%2!=0) :
        while(i>0) :
            if (cont%2!=0) :
                soma = soma-(i%10)
            else :
                soma = soma+(i%10)
        cont = cont+1
        i = i//10
    print(i)