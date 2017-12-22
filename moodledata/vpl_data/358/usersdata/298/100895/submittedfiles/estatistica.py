# -*- coding: utf-8 -*-
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvpad(lista):
    soma = 0
    for i in range (0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    somat = 0
    for i in range (0, len(lista), 1):
        somat = somat + ((lista[i] - resultado)**2)
    d = float(((1/(len(lista)-1))*somat)**(float(1/2))
    return d

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
