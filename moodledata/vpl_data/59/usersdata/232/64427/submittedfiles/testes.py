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
        soma=soma+(lista[i]**2)
    return(soma)

n0=int(input('digito: '))
lista=listaDigitos(n)
print(lista)
print(somaQuadrados(lista))

def feliz(n):
    felicidade=bool(False)
    while felicidade==False:
        digitosN=listaDigitos(n)
        n1=somaQuadrados(digitos)
        if n1==1:
            felicidade=True
            return(True)
        n=somaQuadrados(digitos)    
    return(False)        

if feliz(n):
    print('Feliz')
else:
    print('Infeliz')