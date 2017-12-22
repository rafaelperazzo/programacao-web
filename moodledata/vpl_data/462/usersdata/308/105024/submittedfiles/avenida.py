# -*- coding: utf-8 -*-
def inteiro(texto, min, max):
    valor = int(input(texto))
    while not(min<=valor<=max):
        valor = int(input(texto))
    return valor
    
m = inteiro('Informe a quantidade de quadras no sentido Norte-Sul: ', 2, 1000)
print(m)