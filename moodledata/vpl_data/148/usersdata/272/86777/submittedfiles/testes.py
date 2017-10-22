# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def impar(x):
    if ((x%2)!=0):
        return (True)
    else:
        return (False)
        
for i in range (1000,10000,1):
    if (impar(i)):
        a=i//1000
        b=(i//100)-(a*10)
        c=(i//10)-(a*100)-(b*10)
        d=i-(a*1000)-(b*100)-(c*10)
        if ((a-b+c-d)<0):
            print(i)
        

    

