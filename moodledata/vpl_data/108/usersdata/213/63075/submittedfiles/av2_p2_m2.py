# -*- coding: utf-8 -*-
def calcularVidas(lista,portaEntrada,portaSaida):
    somaDasVidas=0
    for i in range(portaEntrada,portaSaida+1,1):
        somaDasVidas=somaDasVidas+lista[i]
    return(somaDasVidas)
    
quantidadeDeSalas=int(input('Informe a quantidade de salas: '))
lista=[]
for i in range(0,quantidadeDeSalas,1):
    quantidadeDeVidas=int(input('Informe a quantidade de vidas de cada sala: '))
    lista.append(quantidadeDeVidas)
portaEntrada=int(input('Informe a sala de entrada: '))
portaSaida=int(input('Informe a sala de saída: '))

total=calcularVidas(lista,portaEntrada,portaSaida)
print(total)

