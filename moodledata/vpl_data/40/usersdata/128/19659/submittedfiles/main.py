# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

def pi(m):
    
    d=2
    s=1
    soma=3
    # 'd' é a variável usada para controlar o valor dos termos do denominador
    # 's' é a variável usada para controlar o sinal de cada termo
    # 'soma' é a soma dos termos
    
    for i in range (0,m,1):
        soma=soma+((4/(d*(d+1)*(d+2)))*s)
        d=d+2
        s=s*(-1)
    
    return soma
    
def cosseno(x,e):
    
    d=2
    soma=1
    cont=0
    # 'd' é a variável usada para controlar o valor do expoente e do denominador
    # 'soma' é a soma dos termos
    # 'cont' auxilirá no sinal de cada termo

    while True:
        
        fatorial=1
        for i in range(d,0,-1):
            fatorial=fatorial*i
        
        termo=((x**d)/fatorial)
        cont=cont+1
        
        if cont%2==0:
            soma=soma+termo
        
        else:
            soma=soma-termo
        
        if termo<=e:
            break
        
        d=d+2
    
    return soma


m=input('Digite o número m de termos da fórmula de pi: ')

print ('%.15f' %funcoes.pi(m))

e=input('Digite o epsilon para o calculo da razão aurea: ')

x=funcoes.pi(m)/5

print ('%.15f' %(2*funcoes.cosseno(x,e)))
