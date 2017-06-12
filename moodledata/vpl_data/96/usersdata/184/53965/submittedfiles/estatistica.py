# -*- coding: utf-8 -*-


def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    resultado = soma/len(a)
    return resultado
def variância(a):
    media=media(a)
    soma=0
    variância=0
    for i in range(0,len(a),1):
        soma=((a[i]-media)**2)
    variancia=soma/float(len(a))
    return variancia
def desviopadrao(a):
    return math.sqrt(variancia(a))
a=[]
b=[]
n=int(input('digite a quantidade de elementos:'))
for i in range(0,n,1):
    a.append(input('digite um elemnto:'))
for i in range(0,n,1):
    b.append(input('digite um elemnto:'))
media_a=media(a)
media_b=media(b)
desviopadrao_a=desviopadrao(a)
desviopadrao_b=desviopadrao(b)
print(media_a)
print(desviopadrao_a)
print(media_b)
print(desviopadrao_b)



#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 