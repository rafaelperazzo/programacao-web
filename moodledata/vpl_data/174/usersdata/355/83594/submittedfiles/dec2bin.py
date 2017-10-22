# -*- coding: utf-8 -*-
def digitos(numero):
    cont=0
    while(numero>0):
        cont=cont+1
        numero=numero//10
    return(cont)
    
p=int(input('Digite um número: '))
q=int(input('Digite outro número: '))

cont=digitos(p)
cont2=0
while(q>0):
    if q%(10**(cont))==p:
        cont2=cont2 + 1
        q//10
if cont2==0:
    print ('S')
else:
    print('N')

