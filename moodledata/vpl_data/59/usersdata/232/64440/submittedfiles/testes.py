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
'''lista=listaDigitos(n)
print(lista)
print(somaQuadrados(lista))'''

'''def feliz(n):
    felicidade=bool(False)
    while felicidade==False:
        digitosN=listaDigitos(n)
        n1=somaQuadrados(digitosN)
        if n1==1:
            felicidade=True
            return(True)
        n=somaQuadrados(digitosN)
    return(False)        '''
    
def feliz(n):
    cont=0
    while n>0:
        digitosN=listaDigitos(n)
        n1=somaQuadrados(digitosN)
        if n1==1:
            cont=cont+1
        else:
            cont=cont
    if cont=1:
        return(True)
    else:
        return(False)

if feliz(n0):
    print('Feliz')
else:
    print('Infeliz')