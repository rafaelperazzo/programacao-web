
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

def somaQuadrados(digitos):
    soma=0 
    for i in range(0,len(digitos),1):
        soma=soma+(digitos[i]**2)
    return(soma)
    
def repete(n):
    cont=0
    for i in range (0,len(f),1):
        if n==f[i]:
            cont=cont+1
        else:
            cont=cont
    if cont>1:
        return(True)
    else:
        return(False)
        
'''lista=listaDigitos(n)
print(lista)
print(somaQuadrados(lista))'''

def feliz(n):
    f=[]
    cont=0
    felicidade=bool(False)
    while felicidade==False:
        digitosN=listaDigitos(n)
        n1=somaQuadrados(digitosN)
        f.append(n1)
        if n1==1:
            felicidade=True
            return(True)
        for i in range(0,len(f),1):
            if n==f[i]:
                cont=cont+1
            else:
                cont=cont
        if cont>1:
            return(False)
        n=somaQuadrados(digitosN)

n0=int(input('digito: '))


if feliz(n0):
    print('Feliz')
else:
    print('Infeliz')