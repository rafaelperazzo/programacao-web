# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

'''
FUNÇÃO PARA CALCULAR PI
'''
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


    
'''
FUNÇÃO PARA CALCULAR O FATORIAL DO DENOMINADOR DOS TERMOS DA FUNÇÃO COSSENO
'''
    
def fatorial(x):
    
    fatorial=1
    for i in range(x,0,-1):
        fatorial=fatorial*i
        
    return fatorial



'''
FUNÇÃO PARA CALCULAR O COSSENO
'''

def cosseno(x,e):
    
    d=2
    soma=1
    cont=0
    # 'd' é a variável usada para controlar o valor do expoente e do denominador
    # 'soma' é a soma dos termos
    # 'cont' auxilirá no sinal de cada termo

    while True:
        
        termo=((x**d)/fatorial(d))
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

print ('%.15f' %pi(m))

e=input('Digite o epsilon para o calculo da razão aurea: ')

x=pi(m)/5

print ('%.15f' %(2*cosseno(x,e)))
