# -*- coding: utf-8 -*-
N=int(input('digite n:'))
x1=int(input('digite um numero:))
x2=int(input('digite um numero:))
x3=int(input('digite um numero:))
x4=int(input('digite um numero:))
x5=int(input('digite um numero:))
y1=int(input('digite um numero:))
y2=int(input('digite um numero:))
y3=int(input('digite um numero:))
y4=int(input('digite um numero:))
y5=int(input('digite um numero:))
media=(x1+x2+x3+x4+x5)/5
a1=(x1-media)**2
a2=(x2-media)**2
a3=(x3-media)**2
a4=(x4-media)**2
a5=(x5-media)**2
variancia=(a1+a2+a3+a4+a5)/4
dp=variancia**0.5
print('%.2f'%media)
print('%.2f'%dp)
media2=(y1+y2+y3+y4+y5)/5
b1=(y1-media2)**2
b2=(y2-media2)**2
b3=(y3-media2)**2
b4=(y4-media2)**2
b5=(y5-media2)**2
variancia2=(b1+b2+b3+b4+b5)/4
dp2=variancia2**0.5
print('%.2f'%media2)
print('%.2f'%dp2)


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 