# -*- coding: utf-8 -*-
from __future__ import division
import funcoes



#ENTRADA TESTE
f = 0.2
dH = 5
L = 3250
Q = 0.005
g = 9.81
v = 0.000001
E = 0.00006
k = 10
#A saida para esta entrada é aproximadamente: 0.1247 (D) e 0.0224 (f)

Di=D(f,L,Q,g,dH)
R=Rey(Q,Di,v)
Diametro=D(f,L,Q,g,dH)
print ('%.10f ' %Diametro)

fn=F(R,E)
print ('%.10f ' %fn)






'''
k=10
for i in range(0,k,1):
    
    f = 0.2
    dH = input('Digite a perda de carga: ')
    L = input('Digite o comprimento da tubulação: ')
    Q = input('Digite a vazão: ')
    g = input('Digite a gravidade: ')
    v = input('Digite a viscosidade cinemática: ')
    E = input('Digite a rugosidade absoluta: ')
    
  
    
    print ('% .10f ' %funcoes.f2)
   
'''    

    
































































