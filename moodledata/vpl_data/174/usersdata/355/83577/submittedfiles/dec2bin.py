# -*- coding: utf-8 -*-
def digitos(numero):
    cont=0
    while(numero>0):
        cont=cont+1
        numero=numero//10
    return(cont)
    
p=int(input('Digite um número: '))
q=int(input('Digite outro número: '))

cont=digitos(b)
cont2=0
while(a>0):
    if p%(10**(cont))==q:
        cont2=cont2 +1
if cont2==0:
    print ('S')
else:
    print('N')

