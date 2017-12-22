# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a = float(input('Digite o valor de a : '))
b = float(input('Digite o valor de b : '))
precisão = float(input('Digite o valor da precisão : '))

#ARIT
def arit (a,b) :
    while (a>b) and (a-b>precisão) :
        a1 = (1/2) * (a+b)
        b1 = (a*b)**(0.5)
        a = a1
        b = b1
        arit = a1
    return(arit)
print(arit(a,b))
    
        
    
    

