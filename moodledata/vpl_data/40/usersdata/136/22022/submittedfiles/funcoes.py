#ARQUIVO COM SUAS FUNCOES
from __future__ import division

#Na função seguinte, calcula-se o valor absoluto da seguinte forma - se o x tiver valor menor que zero, ou seja,
#negativo, o valor absoluto é igual a esse valor negativo de x multiplicado por "-1". A função retorna o valor absoluto
#(módulo) de x.
def calcula_valor_absoluto(x):
    if x < 0:
        x = x*(-1)
        return x

#Na função seguinte, calcula-se o valor de pi da seguinte forma - enquanto x for menor que m, apresenta-se a condição
#"se 1<=m<=200" (bem como retratado no enunciado) - para o índice "i", procede-se da seguinte maneira - se o índice for par
#expressão "expr" toma o lugar do termo negativo, caso contrário (íncide ímpar), positivo.
#Há atualização e no final o valor de pi é igual a 3 + a expressão final.
def calcula_pi(m):
    expr = 0
    i = 1
    x = 2
    while i<=m:
        if 1<=m<=2000: 
            if i%2==0: 
                expr = expr - (4/(x*(x+1)*(x+2)))
            else:
                expr = expr + (4/(x*(x+1)*(x+2)))
        x = x +2
        i = i +1
    calcula_pi = 3 + expr
    return calcula_pi 

#Na função seguinte, calcula-se o fatorial de um número - a função trata-se de, enquanto i menor ou igual a 1, há
#atualização no fatorial que passa a ser igual a "fatorial vezes i".
def fatorial(n):
    fatorial = 1
    i = 1
    while i<=1:
        fatorial = fatorial * i
        i = i +1
    return fatorial

#Na função seguinte, calcula-se o cosseno - a sentença "fracao" cita cada fração assim como consta na expressão "2".
#Enquanto a fração for maior que o epsilon que o usuário entrou, decorre a seguinte condição - para o índice "i" -
#se o índice for ímpar o termo é negativo, se for par é positivo, conforme os índices e termos da expressão "2" do enunciado.
#Enquanto isso, o expoente atualiza (+2), bem como o índice, para assim continuar a repetição.
#No final, o cosseno é igual ao valor acumulado na soma + 1.
def calcula_co_seno(z, epsilon):
    soma = 0
    i = 1
    expoente = 2
    fracao = (z**expoente)/(fatorial(expoente))
    while fracao>epsilon:
        fracao = (z**expoente)/(fatorial(expoente))
        if i%2!=0:
            soma = soma - fracao
        else:
            soma = soma + fracao
        expoente = expoente + 2
        i = i + 1
    cosseno = 1 + soma
    return cosseno

#Na função seguinte, calcula-se a razão áurea da seguinte forma - obedecendo a fórmula da razão "1" (do enunciado), chama-se
#a função cosseno, com a função pi dividida por 5 (presente na fórmula), e o epsilon dado pelo usuário. No final a função
#retorna fi (que possui o valor o cálculo da razão áurea).
def calcula_razao_aurea(m, epsilon):
    fi = 2 * (calcula_co_seno(calcula_pi(m)/5, epsilon))
    return fi
