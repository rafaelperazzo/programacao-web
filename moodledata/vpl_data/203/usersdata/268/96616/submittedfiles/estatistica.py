# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio (med,a):
    soma=0
    for i in range(0,len(a),1):
        soma= soma + (a[i] - med)**2
    delta=(1/(n-1))*soma
    dd=delta**(1/2)
    return(dd)

n=int(input('Digite o numero de termos da lista: '))
a=[]
b=[]

for i in range(0,n,1):
    valora=int(input('Digite a:'))
    a.append(valora)
for i in range(0,n,1):
    valorb=int(input('Digite b:'))
    b.append(valorb)
    
print(media(a))
print(devio(media(a),a))
print(media(b))
print(devio(media(b),b))





        

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 