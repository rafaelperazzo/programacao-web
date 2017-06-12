# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvPad (lista, media):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media)**2)
    variancia=soma/(len(lista)-1)
    desvPad=(variancia**0.5)
    return(desvPad)
    
a=[ ]
b=[ ]
n=int(input('Digite quantidade de elementos das listas: '))

for i in range(1,n+1,1):
    h1=int(input('Digite o elemento '+str(i)+' da lista a: '))
    a.append(h1)

for i in range(1,n+1,1):
    h2=int(input('Digite o elemento '+str(i)+' da lista b: '))
    b.append(h2)
    
print(media(a))
print(desvPad(a))
print(media(b))
print(desvPad(b))

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 