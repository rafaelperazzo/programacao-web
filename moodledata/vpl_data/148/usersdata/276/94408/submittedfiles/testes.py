# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

m = int(input('Digite m:'))








def calcula_pi (m):
    pi = 3
    posicao = 1
    i = 2
    
    while posicao<=m:
        termo = 4/(i*(i+1)*(i+2))
        if (posicao%2!=0):
            pi = pi + termo
        else:
            pi = pi - termo
        posicao = posicao + 1
        i = i + 2
    return (pi)
    
print (calcula_pi (m))
            
