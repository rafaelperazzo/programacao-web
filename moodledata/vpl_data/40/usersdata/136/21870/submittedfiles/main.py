# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI

#Passos que se seguiram: Primeiro - Foi escrito o código para o cálculo do valor absoluto de "x", para o cálculo de Pi (conforme a fórmula "3" do Enunciado do Programa), para o cálculo do cosseno de "z" (conforme a expressão "2" do Enunciado do Programa) e para o cálculo da Razão Áurea (expressa, inclusive no código, pelo símbolo "Fi"); Segundo - Os códigos foram passados para funções; Terceiro - O programa principal foi escrito, com as entradas e variáveis necessárias, e com a saída e as chamadas das funções.

m = input("Digite o número m de termos da fórmula de pi:")
epsilon = input("Digite o epsilon para o calculo da razao aurea:")

print ("Valor aproximado de pi: %.15f" %(funcoes.calcula_pi(m)))
print ("Valor aproximado da razao aurea: %.15f" %(funcoes.calcula_razao_aurea(m, epsilon)))