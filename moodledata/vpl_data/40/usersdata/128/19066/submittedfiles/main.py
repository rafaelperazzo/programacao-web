# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
def pi(m):
    
    d=2
    s=1
    soma=0
    # 'd' é a variável usada para controlar o valor dos termos do denominador
    # 's' é a variável usada para controlar o sinal de cada termo
    # 'soma' é a soma dos termos
    
    for i in range (0,m,1):
        soma=soma+((4/(d*(d+1)*(d+2)))*s)
        d=d+2
        s=s*(-1)
    
    return soma+3

def cosseno(x,e):
    
    d=2
    s=(-1)
    soma=0
    den=1
    # 'd' é a variável usada para controlar o valor do expoente e do denominador
    # 's' é a variável usada para controlar o sinal de cada termo
    # 'soma' é a soma dos termos
    # 'den' é o valor do denominador

    while True:
        
        for i in range (d,0,-1):
            den=den*i
        
        termo=((x**d)/den)*s
        soma=soma+termo
        
        if termo<e:
            break
        
        s=s*(-1)
        d=d+2
    
    return soma+1

m=input('Digite o número m de termos da fórmula de pi: ')

print ('%.15f' %pi(m))

e=input('Digite o epsilon para o calculo da razão aurea: ')

x=pi(m)/5

resultado=cosseno(x,e)*2

print ('%.15f' %resultado)