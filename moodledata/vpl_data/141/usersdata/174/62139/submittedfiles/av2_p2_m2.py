# -*- coding: utf-8 -*-
def vidas(a,b): # Definindo a função que calcula a quantidade de vidas 
    soma = 0
    for i in range(a,b+1,1):
        soma=soma+a[i]
    print(soma)

# Pedir ao usuário a quantidade de salas(tamanho da lista)
n = int(input('Digite a quantidade de salas: '))
# Criar a lista vázia
a=[]
# Pedir ao usuário a quantidade de vidas de cada sala(elementos da lista)
for i in range(0,n,1):
    a.append(int(input('Quantidade de vidas da %dª sala: '%i)))
# Pedir ao usuário para informar as portas de entrada e saída:
x = int(input('Digite o número da porta de entrada: '))
y = int(input('Digite o número da porta de saída: '))
# Chamar a função para calcular a quantidade de vidas
vidas(x,y)