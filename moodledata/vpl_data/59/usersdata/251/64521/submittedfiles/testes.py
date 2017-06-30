# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def listaDigitos(n):
    d=[]
    while n>0:
        m=n%10
        d.append(m)
        n=n//10
    d.reverse()
    return(d)
    
def somaQuadrados(d):
    soma=0
    for i in range(0,len(d),1):
        soma=soma+(d[i]**2)
    return(soma)

digitos=listaDigitos(n)
print(somaQuadrados(digitos))
    
n = int(input('Digite o valor '))

