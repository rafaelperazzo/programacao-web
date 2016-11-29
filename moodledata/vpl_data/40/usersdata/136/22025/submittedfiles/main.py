# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
#Passos que se seguiram: Primeiro - Foi escrito o código para o cálculo do valor absoluto de "x", para o cálculo de Pi
#(conforme a fórmula "3" do Enunciado do Programa), para o cálculo do cosseno de "z" (conforme a expressão "2" do Enunciado do Programa)
#e para o cálculo da Razão Áurea (expressa, inclusive no código, pelo símbolo "Fi"); Segundo - Os códigos foram passados para funções;
#Terceiro - O programa principal foi escrito, com as entradas e variáveis necessárias, e com a saída e as chamadas das funções.

#Comentários sobre as funções.
#Na função "calcula_valor_absoluto(x)", calcula-se o valor absoluto da seguinte forma - se o x tiver valor menor que zero, ou seja,
#negativo, o valor absoluto é igual a esse valor negativo de x multiplicado por "-1". A função retorna o valor absoluto
#(módulo) de x.

#Na função "calcula_pi(m)", calcula-se o valor de pi da seguinte forma - enquanto x for menor que m, apresenta-se a condição
#"se 1<=m<=200" (bem como retratado no enunciado) - para o índice "i", procede-se da seguinte maneira - se o índice for par
#expressão "expr" toma o lugar do termo negativo, caso contrário (íncide ímpar), positivo.
#Há atualização e no final o valor de pi é igual a 3 + a expressão final.

#Na função "fatorial(n)", calcula-se o fatorial de um número - a função trata-se de, enquanto i menor ou igual a 1, há
#atualização no fatorial que passa a ser igual a "fatorial vezes i".

#Na função "calcula_co_seno(z, epsilon)", calcula-se o cosseno - a sentença "fracao" cita cada fração assim como consta na expressão "2".
#Enquanto a fração for maior que o epsilon que o usuário entrou, decorre a seguinte condição - para o índice "i" -
#se o índice for ímpar o termo é negativo, se for par é positivo, conforme os índices e termos da expressão "2" do enunciado.
#Enquanto isso, o expoente atualiza (+2), bem como o índice, para assim continuar a repetição.
#No final, o cosseno é igual ao valor acumulado na soma + 1.

#Na função "calcula_razao_aurea(m, epsilon)", calcula-se a razão áurea da seguinte forma - obedecendo a fórmula da razão "1" (do enunciado), chama-se
#a função cosseno, com a função pi dividida por 5 (presente na fórmula), e o epsilon dado pelo usuário. No final a função
#retorna fi (que possui o valor o cálculo da razão áurea).

#PS: Estava dando erro ao colocar esses comentários em "funcoes.py", por isto estão aqui.

m = input("Digite o número m de termos da fórmula de pi:")
epsilon = input("Digite o epsilon para o calculo da razao aurea:")

print ("Valor aproximado de pi: %.15f" %funcoes.calcula_pi(m))
print ("Valor aproximado da razao aurea: %.15f" %funcoes.calcula_razao_aurea(m, epsilon))