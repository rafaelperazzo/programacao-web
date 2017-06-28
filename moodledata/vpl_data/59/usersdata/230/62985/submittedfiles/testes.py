# -*- coding: utf-8 -*-
import math
''' Definição: O programa tem a função de determinar se um número é Feliz ou não,recebendo um número e fazendo 
a soma do quadrado dos seus termos, até que obtenha um último termo e por fim verifique se é igual a 1 
(sendo assim um número Feliz) ou diferente de 1 (não é feliz). 

    Na primeira função, enquanto o valor de 'n' for diferente de 0 será dividido por 10, para ter os termos 
separados e assim adicionados na lista. A lista receberá o resto da divisão inteira por 10. E por fim retornará a lista 'a'.
    Na segunda função ele fará a soma dos quadrados dos termos da lista 'a' da primeira função e retornará o valor da soma. 
    
    O valor de n será dividido por 10 e chamará as duas funções (separar os termos, adicioná-los à lista e fazer a soma do quadrado
dos termos) até que se obtenha  um valor para n onde a divisão inteira por 10 seja 0. Pois o objetivo é chegar à apenas um termo
para comparar se ele é diferente de 1 ou não.
    'b' receberá a função 'algarismo' que será parâmetro da função 'soma2'. E por fim 'n' receberá esta soma de 'b'. E quando 'n' chegar 
a um termo, passará pela condição para determinar se é ou não número Feliz. '''

def algarismo(n):
    a=[]
    while(n!=0) :
        a.append(n%10)
        n=n//10
    return(a)
    
def soma2(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+(a[i])**2
    return(soma)
    
n=int(input('Digite valor: '))

while n//10!=0:
    b=algarismo(n)
    n=soma2(b)
if n==1:
    print('Feliz')
if n!=1:
    print('Não Feliz')

