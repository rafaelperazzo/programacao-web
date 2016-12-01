# -*- coding: utf-8 -*-
from __future__ import division
import funcoes


'''
ENTRADA TESTE
f = 0.2
dH = 5
L = 3250
Q = 0.005
g = 9.81
v = 0.000001
E = 0.00006
k = 10
A saida para esta entrada é aproximadamente: 0.1247 (D) e 0.0224 (f)
'''

k=10 # De acordo com a descrição, o número de interações corresponde a um valor fixo, portanto, não é pedido ao usuário
f = 0.2 # a variável é um valor fixo
dH = input('Digite a perda de carga: ')
L = input('Digite o comprimento da tubulação: ')
Q = input('Digite a vazão: ')
g = input('Digite a gravidade: ')
v = input('Digite a viscosidade cinemática: ')
E = input('Digite a rugosidade absoluta: ')

for i in range(0,k,1):
    
    Di=funcoes.D(f,L,Q,g,dH) # Chamando a função em outro arquivo do Python
    R=funcoes.Rey(Q,Di,v) # Chamando a outra funcao do mesmo arquivo: funcoes
    
    Diametro=funcoes.D(f,L,Q,g,dH) # Substituindo os valores fornecidos pelo usuário nas funcoes
    fn=funcoes.F(R,E,Di) # Substituindo os valores fornecidos pelo usuário nas funcoes
    
    if f==fn:
        break
        print ('%.10f ' %Diametro) # Mostrando o resultado com 10 casas decimais
        print ('%.10f ' %fn) # Mostrando o resultado com 10 casas decimais 
    else:
        f=fn
    
    

    
































































