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

n=int(input('digito '))
print(listaDigitos(n))    