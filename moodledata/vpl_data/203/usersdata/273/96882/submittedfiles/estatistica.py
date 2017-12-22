# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
lista=[]
n1=int(input('Digite a quantidade de termos: '))
soma1=0

for i in range (0,n,1):
    numero1=int(input('Digite o numero: '))
    lista.append(numero)
    soma1=soma1+numero

media1=soma1/n
somatorio1=0

for l in range(0,n,1):
    somatorio1=somatorio1+((list1(l)-media1))**2

desvio1=((1)/(n-1)*(somatorio1)**0.5

#para a lista 2

listb=[]
n2=int(input('Digite a quantidade de termos: '))
soma2=0

for i in range (0,n,1):
    numero2=int(input('Digite o numero: '))
    listb.append(numero)
    soma2=soma2+numero

media2=soma2/n
somatorio2=0

for l in range(0,n,1):
    somatorio2=somatorio2+((list2(l)-media2))**2

desvio2=((1)/(n-1)*(somatorio2)**0.5
print('%.2f'% list1[0])
print('%.2f'% list1[n-1])
print('%.2f'% media1)   
print('%.2f'% desvio1)
print('%.2f'% list2[0])
print('%.2f'% list2[n-1])
print('%.2f'% media2)   
print('%.2f'% desvio2)


print('%.2f'% 
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 