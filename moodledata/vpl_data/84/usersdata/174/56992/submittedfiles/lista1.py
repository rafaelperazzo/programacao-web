# -*- coding: utf-8 -*-

# Criação/definição das funções necessárias
def qimpar(a):
    # Código da função da quantidade de números impares
    cont = 0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            cont=cont+1
    print (cont)

def qpar(a):
    # Código da função da quantidade de números pares
    cont = 0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            cont=cont+1
    print (cont)

def simpar(a):
    # Código da função da soma dos números impares
    soma = 0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            soma=soma+a[i]
    print (soma)

def spar(a):
    # Código da função da soma dos números pares
    soma = 0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            soma=soma+a[i]
    print (soma)

# Pedir ao usuário para informar o tamanho da lista
n=int(input('Quantidade de elementos da lista: '))

# Criar a lista vazia
a=[]
# Pedir a inserção de elementos à lista ao usuário
for i in range(1,n+1,1):
    a.append(int(input('%dº Elemento: '%i)))
    
# Processamento - Chamando as funções
simpar(a)   # Somatório dos números impares
spar(a)     # Somatório dos números pares
qimpar(a)   # Quantidade de números impares
qpar(a)     # Quantidade de números pares
print (a)   # Impressão da lista