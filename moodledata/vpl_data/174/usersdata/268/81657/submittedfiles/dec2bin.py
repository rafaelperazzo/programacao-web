# -*- coding: utf-8 -*-

def digitos (numero):
    cont=0
    while(numero>0):
        numero=numero//10
        cont=cont+1
    return (cont)

p=int(input('Digite p : '))
q=int(input('Digite q : '))

while ():
    x9= digitos(p)
    if (q%10**x9)==p:
        print('S')
    else: 
        print('N')
    
