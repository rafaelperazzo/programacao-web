# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

#criando uma função para transformar o número em uma lista
def lista(numero): #recebendo um parâmetro e o aplicando a função
    lista = [] #iniciando uma lista vazia
    cont=0     #iniciando um contador
    while numero > 0: #comando para que o processamento dentro da tabulação seja executado enquanto atender a condiçao
        resto = numero%10 #obtendo o resto da divisão do dado de entrada por 10
        cont = cont+1 #atualizando o contador
        lista.insert(0,resto) #inserindo o resto obtido anteriormente em uma lista
        numero = numero//10 #atualizando o dado de entrada
    return (lista,cont) #após a execução da condição acima, retorna-se dois parâmetros da função, uma lista e o contador
    
#função para determinar se o número é feliz ou não#
def feliz(numero):
    lista_b = []
    while numero > 0:
        soma = 0
        lista_a = lista(numero)[0]
        for i in range(0,len(lista_a),1):
            soma = soma+lista_a[i]**2
        lista_b.append(soma)
        if lista_b[len(lista_b)-1] == 1:
            return(True,lista_b)
        elif lista_b[len(lista_b)-1] == 16:
            return (False,lista_b)
        numero = soma
    
print(' Números felizes são números cujo a soma dos quadrados dos seus termos gera um novo número e, esse novo número deve satizfazer a afirmação anterior até que a soma dê o número "1".')

numero=int(input('Baseado na definição de número feliz, digite um número à ser testado:'))

if feliz(numero)[0]:
    print('SIM, o número testado é feliz! E esta lista de números abaixo contém as somas dos quadrados dos seus algarismos, e por consequência, também são felizes:')
    print(feliz(numero)[1])
else:
    print('NÃO, o número testado não é feliz! E esta lista de números abaixo contém algumas das somas dos quadrados dos seus algarismos, e por consequência, também não são felizes:')
    print(feliz(numero)[1])
    

    
    
    
    
    
    
    
    
