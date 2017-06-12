# -*- coding: utf-8 -*-
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista):
    soma=0
    for i in range(0,len(lista),1):
        a=(lista[i]-media)**2
        soma=soma+a
    variancia=soma/(len(lista)-1)
    desvio=variancia**(0.5)
    return desvio
n=int(input('Digite o número de termos das listas: '))
a=[]
b=[]
for i in range(1,n+1,1):
    termoa=float(input('Termo da primeira lista: '))
    a.append(termoa)
for i in range(1,n+1,1):
    termob=float(input('Termo da segunda lista: '))
    b.append(termob)
print('%.2f'%media(a))
print('%.2f'%desvio(a))
print('%.2f'%media(b))
print('%.2f'%desvio(b))

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 