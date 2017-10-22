# -*- coding: utf-8 -*-
def digitos(numero):
    cont=0
    while(numero>0):
        cont=cont+1
        numero=numero//10
    return(cont)
    
p=int(input('Digite o suposto subnúmero: '))
q=int(input('Digite o número principal: '))

digp=digitos(p)
cont=0
while(q>p):
    if q%(10**(digp))==p:
        cont=cont + 1
    q//10
if cont!=0:
    print ('s')
else:
    print('n')

