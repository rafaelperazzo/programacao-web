# -*- coding: utf-8 -*-
def calcularVidas(lista,portaEntrada,portaSaida):
    somaDasVidas=0
    for i in range(portaEntrada,portaSaida+1,1):
        somaDasVidas=somaDasVidas+lista[i]
    return(somaDasVidas)
    

lista=[]


