# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

#criando uma função para transformar o número em uma lista
def lista(numero):            #recebendo um parâmetro e o aplicando a função
    lista = []                #iniciando uma lista vazia
    cont=0                    #iniciando um contador
    while numero > 0:         #comando para que o processamento dentro da tabulação seja executado enquanto atender a condiçao
        resto = numero%10     #obtendo o resto da divisão do dado de entrada por 10
        cont = cont+1         #atualizando o contador
        lista.insert(0,resto) #inserindo o resto obtido anteriormente em uma lista
        numero = numero//10   #atualizando o dado de entrada
    return (lista,cont)       #após a execução da condição acima, retorna-se dois parâmetros da função, uma lista e o contador
    
#função para determinar se o número é feliz ou não
def feliz(numero):                          #recebendo um parâmetro e o aplicando a função     
    lista_b = []                            #iniciando uma lista vazia
    while numero > 0:                       #comando para que o processamento dentro da tabulação seja executado enquanto atender a condiçao
        soma = 0                            #iniciando um samatório
        lista_a = lista(numero)[0]          #chamando a função lista e guardado em uma variável o seu parâmetro da posição [0]
        for i in range(0,len(lista_a),1):   #repetição entre 0 e o número equivalente ao tamanho da lista, variando de 1 em 1
            soma = soma+lista_a[i]**2       #somando os quadrados dos termos do dado de entrada
        lista_b.append(soma)                #guardando cada somatório em uma nova lista
        if lista_b[len(lista_b)-1] == 1:    #condição para que o dado de entrada seja um número feliz
            return(True,lista_b)            #retornando 'verdadeiro' caso a condição anterior seja atendida
        elif lista_b[len(lista_b)-1] == 4: #condição para que o dado de entrada não seja um número feliz
            return (False,lista_b)          #retornando 'falso' caso a condição anterior seja atendida
        numero = soma                       #atualização do número á ser testado

#definição de número feliz será impressa na tela
print(' Números felizes são números cujo a soma dos quadrados dos seus termos gera um novo número e, esse novo número deve satizfazer a afirmação anterior até que a soma dê o número "1".')

#dado de entrada
numero=int(input('Baseado na definição de número feliz, digite um número à ser testado:'))
#testando se o dado de entrada é feliz, chamndo assim, a função 'feliz(numero)'
if feliz(numero)[0]:
    print('SIM, o número testado é feliz! E esta lista de números abaixo contém as somas dos quadrados dos seus algarismos, e por consequência, também são felizes:')
    print(feliz(numero)[1])
#condição contrária. Caso a condição aterior não for atendida esta entrará em vigor
else:
    print('NÃO, o número testado não é feliz! E esta lista de números abaixo contém algumas das somas dos quadrados dos seus algarismos, e por consequência, também não são felizes:')
    print(feliz(numero)[1])
    

    
    
    
    
    
    
    
    
