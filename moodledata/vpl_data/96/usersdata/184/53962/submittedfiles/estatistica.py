# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def variância(lista):
    media=media(lista)
    soma=0
    variância=0
    for i in range(0,len(lista),1):
        soma=((lista[i]-media)**2)
    variancia=soma/float(len(lista))
    return variancia
def desviopadrao(lista):
    return math.sqrt(variancia(lista))
a=[]
b=[]
n=int(input('digite a quantidade de elementos:'))
for i in range(0,n,1):
    a.append(input('digite um elemnto:'))
for i in range(0,n,1):
    b.append(input('digite um elemnto:'))
media_a = media(a)
media_b = media(b)
desviopadrao_a=desviopadrao(a)
desviopadrao_b=desviopadrao(b)
print(media_a)
print(desviopadrao_a)
print(media_b)
print(desviopadrao_b)



#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 