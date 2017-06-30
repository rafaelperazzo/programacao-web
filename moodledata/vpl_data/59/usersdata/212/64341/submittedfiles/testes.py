# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

print ('O programa a seguir mostrará se um número é ou não Feliz.')
print ('A condição para que um número seja Feliz é: um número inteiro positivo, o número é substituido pela soma dos quadrados dos seus dígitos e repete-se o processo até que o número seja igual a 1 ou até que entre num ciclo infinito')

def repete (lista, numero):
    cont = 0
    for i in range (0,len(lista),1):
        if numero == lista[i]:
           cont = cont + 1
    if cont > 1:
        return True
    else:    
        return False
        
        
n = int(input('Digite um valor:'))
a = []
x = n
i = 1
while i != 0:
    ne = 0
    num = n
    ne = 1
    while (num//10) > 0:
        ne = ne + 1
        num = num//10
    soma = 0
    i = ne - 1
    while i >= 0:
        e = n//(10**i)
        soma = soma + (e**2)
        n = n% (10**i)
        i= i - 1
    print (soma)
    n = soma
    a.append(n)
    if n == 1:
        print ('Número Feliz')
        break
    elif repete (a,n):
        print ('Não é um Número Feliz')
        break
