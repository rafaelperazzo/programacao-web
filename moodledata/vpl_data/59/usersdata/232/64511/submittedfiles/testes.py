
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
    f=[]
    soma=0 
    for i in range(0,len(digitos),1):
        soma=soma+(digitos[i]**2)
        f.append(soma)
    return(soma,f)
    
def repete(f,n):
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
    felicidade=bool(False)
    while felicidade==False:
        digitosN=listaDigitos(n)
        n1=somaQuadrados(digitosN)[0]
        f1=somaQuadrados(digitosN)[1]
        if n1==1:
            felicidade=True
            return(True)
        if repete(f1,n):
            return(False)
        n=somaQuadrados(digitosN)

n0=int(input('digito: '))
digitosN=listaDigitos(n0)
n1=somaQuadrados(digitosN)[0]
f1=somaQuadrados(digitosN)[1]
print(digitosN)
print(n1)
print(f1)


if feliz(n0):
    print('Feliz')
else:
    print('Infeliz')