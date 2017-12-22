# -*- coding: utf-8 -*-
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvpad(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    somat=0
    for i in range (0, len(lista), 1):
        somat+=((lista[i] - resultado)**2)
    desv = float(((1/(len(lista)-1))*somat)**(float(1/2))
    return desv

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

lista=[0, 1, 2, 3]
print(media(lista))
print(desvpad(lista))