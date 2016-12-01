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
#negativo, a função retorna esse valor multiplicado por "-1". Caso contrário, ou seja, x positivo, a função retorna o próprio x.

#Na função "calcula_pi(m)", calcula-se o valor de pi da seguinte forma - enquanto x for menor que m, apresenta-se a condição
#"se 1<=m<=200" (bem como retratado no enunciado) - para o índice "i", procede-se da seguinte maneira - se o índice for par
#expressão "expr" toma o lugar do termo negativo, caso contrário (íncide ímpar), positivo.
#Há atualização e no final o valor de pi é igual a 3 + a expressão final.

#Na função "fatorial(n)", calcula-se o fatorial de um número - a função trata-se de, começando em n e decrescendo até 1, há 
#atualização na base que passa a ser igual a "base vezes i" - ou seja, o produto dos n números começando em n e decrescendo até 1.

#Na função "calcula_co_seno(z, epsilon)", calcula-se o cosseno - primeiramente, precisa-se de algumas variáveis (cont, resultado e multiplicacao), 
#enquanto o epsilon (que o usuário entrou) for menor que o contador(cont), conta mais um, e segue - se cont for par, a atualização
#será para negativo, se for ímpar, será para positivo. A sentença anterior se confirma, com a variável "resultado" que chama as funções "calcula_valor_absoluto(x)"
#e "fatorial(n)". Após as repetições, retorna o resultado acumulado.
#NOTA - Nesse código eu procurei chamar as funções não 'usadas' até então (fatorial e calcula_valor_absoluto). Sendo assim, procurei
#não utilizar um código que trabalhasse uma determinada variável e ao final somasse com "1". Ou seja, no índice 0, (z^0)/0! que é igual a 1,
#então, não precisando mais somar a 1 no final.

#Na função "calcula_razao_aurea(m, epsilon)", calcula-se a razão áurea da seguinte forma - obedecendo a fórmula da razão "1" (do enunciado), chama-se
#a função cosseno, com a função pi dividida por 5 (presente na fórmula), e o epsilon dado pelo usuário. No final a função
#retorna fi (que possui o valor o cálculo da razão áurea).

#PS: Esses comentários estavam postos conforme a disposição das funções, mas como estava dando erro em "funcoes.py", compilei-os aqui.

m = input("Digite o número m de termos da fórmula de pi:")
epsilon = input("Digite o epsilon para o calculo da razao aurea:")

print ("Valor aproximado de pi: %.15f" %funcoes.calcula_pi(m))
print ("Valor aproximado da razao aurea: %.15f" %funcoes.calcula_razao_aurea(m, epsilon))