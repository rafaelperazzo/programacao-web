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

def feliz(n):
    inicial=n
    felicidade=bool(False)
    while felicidade==False:
        digitosN=listaDigitos(n)
        n1=somaQuadrada(digitosN)
        if n1==1:
            felicidade=True
            return(True)
        elif n1==inicial:
            felicidade=True
            return(False)
        n=n1        

n=int(input('Digite o numero: '))
if feliz(n):
    print('Feliz')
else:
    print('Infeliz')

