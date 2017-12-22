# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista

def somatorio(a,media):
    soma2=0
    for i in range(0,n,1):
        soma=(((a[i])-media)**2)
        soma2=soma2+soma
    return(soma2)

def desvio(a,n,media):
    desviopad=((1/(n-1))*(somatorio(a,media)))**(0.5)
    return(desviopad)

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas.

a=[]
b=[]
n=int(input('Digite a quantidade de números de a: '))

for quant in range(0,n,1):
    num=float(input('Digite um valor: '))
    a.append(num)
    
m=int(input('Digite a quantidade de números de b: '))
    
for quant2 in range(0,m,1):
    num=float(input('Digite um valor: '))
    b.append(num)
    
print(media(a))
print(desvio(a,n,media(a)))

print(media(b))
print(desvio(b,m,media(b)))