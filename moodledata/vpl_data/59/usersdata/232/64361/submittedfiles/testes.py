# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def listaDigitos(n):
    digitos=[]
    while n>0:
        m=n%10
        digitos.append(m)
        n=n//10
    digitos.reverse()    
    return(digitos)

def somaQuadrados(lista):
    soma=0 
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    return(soma)

n=int(input('digito '))
lista=listaDigitos(n)
print(lista)
print(somaQuadrados(lista))
