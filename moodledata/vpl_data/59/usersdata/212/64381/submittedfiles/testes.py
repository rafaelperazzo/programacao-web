# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

print ('O programa a seguir mostrará se um número é ou não Feliz.')
print ('''A condição para que um número seja Feliz é: que seja inteiro positivo,
assim, o número é substituido pela soma dos quadrados dos seus dígitos e repete-se o
processo até que o número seja igual a 1 ou até que entre num ciclo infinito.''')

#DEFINIREMOS UMA FUNÇÃO PARA TESTAR SE ALGUM NÚMERO REPETE-SE.
#CASO HAJA REPETIÇÃO, O PROGRAMA ENTRARÁ EM UM LOOPING INFINITO.
#E ISSO É O QUE QUEREMOS EVITAR.

def repete (lista, numero):
    cont = 0
    for i in range (0,len(lista),1):
        if numero == lista[i]:
           cont = cont + 1
    if cont > 1:
        return True
    else:    
        return False

#A VARIÁVEL 'n' RECEBERÁ O VALOR DIGITADO PELO USUÁRIO.        
        
n = int(input('Digite um valor:'))

#SERÁ DEFINIDA UMA LISTA 'a' PARA FUTURAMENTE RECEBER OS VALORES DAS OPERAÇÕES AOS QUAIS SERÃO TESTADOS SE REPETEM-SE OU NÃO.

a = []

#'i' SERÁ A VARIÁVEL DE CONTROLE PARA O WHILE.

i = 1

#ENQUANTO 'i' DIFERIR DE ZERO, A CONDIÇÃO ABAIXO CONTARÁ A QUANTIDADE DE ALGARISMOS QUE CONSISTE O NÚMERO E ELEVARÁ CADA UM AO QUADRADO E FARÁ O SOMATÓRIO DOS QUADRADOS.

while i != 0:
    ne = 0
    num = n
    ne = 1
    
    #A CONDIÇÃO ABAIXO DEFINIRÁ A QUANTIDADE DE ALGARISMOS.
    
    while (num//10) > 0:
        ne = ne + 1
        num = num//10
    soma = 0
    i = ne - 1
    
    #ESTA CONDIÇÃO ELEVARÁ CADA ALGARISMO AO QUADRADO E EXECUTARÁ O SOMATÓRIO.
    
    while i >= 0:
        e = n//(10**i)
        soma = soma + (e**2)
        n = n% (10**i)
        i= i - 1
    print (soma)
    n = soma
    
    #O INCREMENTO DA LISTA SERÁ FEITO PARA NÃO PERDERMOS OS NÚMEROS ANTERIORMENTE CALCCULADOS PARA PODERMOS TESTAR SE HAVERÁ REPETIÇÃO OU NÃO.
    
    a.append(n)
    
    #O TESTE ABAIXO IDENTIFICARÁ SE O SOMATÓRIO DOS ALGARISMOS AO QUADRADO É IGUAL A 1 (UM).
    #SENDO IGUAL A 1, SERÁ UM NÚMERO FELIZ.
    if n == 1:
        print ('Número Feliz')
        break
    
    #ESTE TESTE CHAMA A FUNÇÃO PARA SABERMOS SE OCORRE OU NÃO UMA REPETIÇÃO DE NÚMEROS NAS OPERAÇÕES.
    #CASO HAJA, O NÚMERO NÃO SERÁ FELIZ.
    elif repete (a,n):
        print ('Não é um Número Feliz')
        break
