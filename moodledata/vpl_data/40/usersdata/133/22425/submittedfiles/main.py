# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#calcula o valor absoluto.
def calcula_valor_absoluto(x):
    if (x<0):
        return (-1)*x
    else:
        return x


#calcula o valor de pi, para m termos especificados.        
def calcula_pi(m):
    pi = 3
    for i in range(1, m + 1, 1):
        pi = pi + (((-1)**(i+1))*4)/((2*i)*(2*i+1)*(2*i+2))
    return pi


#calcula o fatorial de um número.
def fat(x):
    fat = 1
    while (x>0):
        fat = x*fat
        x = x-1
    return fat


#calcula o valor do cosseno de z, para um termo cujo o seu valor absoluto é menor ou iguar ao e.        
def calcula_co_seno(z, e):
    cos_z = 1
    i = 1
    while(cos_z>=-1 and cos_z<=1):
        d = fat(2*i)
        b = (((-1)**i)*((z)**(2*i)))/ d
        c = calcula_valor_absoluto(b)
        if (c<e):
            break
        else:
            cos_z = cos_z + b
        i = i + 1
    return cos_z
    

#Calcula a razão aurea
def calcula_razao_aurea(m, e):
    grad = (calcula_pi(m))/5               #grad é o gradiente, ou seja, o ângulo.
    ra = 2*(calcula_co_seno(grad, e))        #ra é a razão aurea.
    return ra

    
#função main
print('Função para calcular a razão aurea.')
print('Para calarmos a razão aurea precisamos especificar dois parâmetros. Eles são:')
print('n = número de termos a ser considerado na série de pi, tal que n E [1;2000].')
print('e = termo limite para a série do cosseno, tal que e E ]0;1[.')

n = input('Especifique o valor de n:')
while(n<1 or n>2000):
    print('O valor de n não pertence ao intervalo considerado.')
    n = input('Especifique o valor de n:')
    
e = input('Especifique o valor de e:')
while (e<=0 or e>=1):
    print('O valor de e não pertence ao intervalo considerado.')
    e = input('Especifique o valor de e:')
print ('%.15f' %calcula_pi(n))
print ('%.15f' %calcula_razao_aurea(n, e))
