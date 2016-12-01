# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#calcula o valor absoluto.
calcula_valor_absoluto(x):
    if (x<0):
        return (-1)*x
    else:
        return x


#calcula o valor de pi, para m termos especificados.        
calcula_pi(m):
    pi = 3
    for i in range(1, m + 1, 1):
        pi = pi + ((-1)**(i+1))*4)/((2*i)*(2*i+1)*(2*i+2))
    return pi


#calcula o fatorial de um número.
fat(x):
    fat = 1
    while (x>0):
        fat = x*fat
        x = x-1
    return fat


#calcula o valor do cosseno de z, para um termo cujo o seu valor absoluto é menor ou iguar ao e.        
calcula_co_seno(z, e):
    cos_z = 1
    i = 0
    while(cos_z>=-1 and cos_z<=1):
        b = (((-1)**i)*((z)**(i+1)))/ (fat(i+1))
        c = calcula_valor_absoluto(b)
        if (c>e):
            break
        else:
            cos_z = cos_z + b
        i = i + 1
    return cos_z
    

#Calcula a razão aurea
calcula_razao_aurea(m, e):
    grad = (calcula_valor_pi(m))/5        #grad é o gradiente, ou seja, o ângulo.
    ra = 2*(calcula_co_seno(grad))        #ra é a razão aurea.
    return ra

    
#função main
print('Função para calcular a razão aurea.')
print('Para cal
m = input('Especifique o valor de m:')
e = input('Especifique o valor de epsilon:')
print calcula_razao_aurea(m,e)