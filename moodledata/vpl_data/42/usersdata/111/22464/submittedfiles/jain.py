# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

fn = 0.2 # a variável é um valor fixo
dH = input('Digite a perda de carga: ')
L = input('Digite o comprimento da tubulação: ')
Q = input('Digite a vazão: ')
g = input('Digite a gravidade: ')
v = input('Digite a viscosidade cinemática: ')
E = input('Digite a rugosidade absoluta: ')

k=10 # De acordo com a descrição, o número de interações corresponde a um valor fixo, portanto, não é pedido ao usuário
while True:
    f=fn
    Di=funcoes.D(f,L,Q,g,dH) # Chamando a função em outro arquivo do Python
    R=funcoes.Rey(Q,Di,v) # Chamando a outra funcao do mesmo arquivo: funcoes
    
    Diametro=funcoes.D(f,L,Q,g,dH) # Substituindo os valores fornecidos pelo usuário nas funcoes
    fn=funcoes.F(R,E,Di) # Substituindo os valores fornecidos pelo usuário nas funcoes
    
    if abs(f-fn<=0.000000001): #Comparando e igualando a variavel 'f' com 'fn' calculado, de acordo com uma diferença ínfima
        break #Se ambas forem praticamente iguais, encontraremos a solução
    
print ('%.10f ' %Diametro) # Mostrando o resultado com 10 casas decimais
print ('%.10f ' %fn) # Mostrando o resultado com 10 casas decimais 
    
    
        
        
    
    
    

    
































































