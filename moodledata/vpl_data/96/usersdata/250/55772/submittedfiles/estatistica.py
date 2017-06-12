# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
def desPad(lista):
    soma=0
    soma1=0
    for i in range (0,len(lista),1):
        soma=soma+lista[i]
        media=soma/(len(lista))
        soma1=soma1+((lista[i]-media)**2)
        desPad=soma1/(n-1)**(1/2)
    return desPad
    
