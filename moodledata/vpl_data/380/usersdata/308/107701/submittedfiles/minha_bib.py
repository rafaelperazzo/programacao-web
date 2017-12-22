# -*- coding: utf-8 -*-
from random import randint

def testeum():
    a = 10
    print(id(a))
def testedois():
    a = 10
    print(id(a))

def sorteiaReaisVetor(qnt, cd):
    #Primeiro parâmetro: Quantidade de itens || Segundo parâmetro: Quantidade de casas decimais
    notas = []
    for i in range(0, qnt):
        x = randint(0, 100)/float(10**cd)
        notas.append(x)
        
    return notas

def porextenso(x):
    unidade = ['', ' e um', ' e dois', ' e tres',' e quatro', ' e cinco', ' e seis', ' e sete', ' e oito', ' e nove']
    dezena = ['', ' e dez', ' e vinte', ' e trinta',' e quarenta', ' e cinquenta', ' e sessenta', ' e setenta',  ' e oitenta', ' e noventa']
    centena = ['', 'Cento', 'Duzentos', 'Trezentos','Quatrocentos', 'Quinhentos', 'Seiscentos', 'Setecentos', 'Oitocentos', 'Novecentos']
    
    return (centena[int(x[0])] + dezena[int(x[1])] + unidade[int(x[2])])
    
def converterBinario(valor):
    resultado=''
    while valor>1:
        resultado += str(valor%2)
        valor = valor//2
    resultado +='1'
    return resultado[::-1}