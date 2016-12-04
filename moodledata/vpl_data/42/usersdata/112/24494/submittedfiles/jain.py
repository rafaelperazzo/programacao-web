# -*- coding: utf-8 -*-
from __future__ import division
import funcoes
import math


f = 0.2
dH = input('Digite a perda de carga: ')
L = input('Digite o comprimento da tubulação: ')
Q = input('Digite a vazão: ')
g = input('Digite a gravidade: ')
v = input('Digite a viscosidade cinemática: ')
e = input('Digite a rugosidade absoluta: ')
k = 10



'''
A princípio, irei definir as fórmulas que serão ulizadas durante o exercício e que já foram fornecidas no enunciado
'''



D = ((8*f*L*(Q**2))/(dH*(math.pi**2)*g))**(1/5)
Rey = (4*Q)/(math.pi*D*v)
fn = (((64/Rey)**8)+95*(math.log((e/3.1*D)+(5.47/(Rey**0.9)))-(2500/Rey)**6)**-16)**0.125



'''
Feito isso, irei agora definir as restrições que foram pedidas no trabalho. Caso f seja igual fn, o problema acaba e serão 
printados os valores de D e f.
'''

if fn==f:
   
    print D
    print f
    
    
    
'''
Por ultimo, caso fn seja diferente de f, irei definir uma repetição 
para que o problema continue até que atingir a quantidade "K" que foi inserida no princípio.
'''



if fn!=f:

    def definicao_do_D(f, g, v, Q, dH, L,):
        for i in range(0 , k , 1):
            D = ((8*f*L*(Q**2))/(dH*(math.pi**2)*g))**(1/5)
            Rey = (4*Q)/(math.pi*D*v)
            fn = (((64/Rey)**8)+95*(math.log((e/3.1*D)+(5.47/(Rey**0.9)))-(2500/Rey)**6)**-16)**0.125
            f = fn
        return D
        
    def definicao_do_f(f, g, v, Q, dH, L,):
        for i in range(0 , k , 1):
            D = ((8*f*L*(Q**2))/(dH*(math.pi**2)*g))**(1/5)
            Rey = (4*Q)/(math.pi*D*v)
            fn = (((64/Rey)**8)+95*(math.log((e/3.1*D)+(5.47/(Rey**0.9)))-(2500/Rey)**6)**-16)**0.125
            f = fn
        return f
        
    print ('D:%.5f'%definicao_do_D(f,g,v,Q,dH,L,))
    print ('f:%.5f'%definicao_do_f(f,g,v,Q,dH,L,))
