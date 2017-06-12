# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def desvio(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    p=0
    for i in range(0,len(lista),1):
        p=(lista[i]-media)**2+p
    final=p/len(lista)
    return final
        

n=int(input('digite n: '))
lista1=[ ]
for i in range(0,n,1):
    valor=float(input('digite n: '))
    lista1.append('valor')
lista2=[ ]
for i in range(0,n,1):
    valor=float(input('digite n: '))
    lista2.append('valor')
print( 'desvio(lista1)')
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 