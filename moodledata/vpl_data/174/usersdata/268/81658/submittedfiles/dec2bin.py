# -*- coding: utf-8 -*-

def digitos (numero):
    cont=0
    while(numero>0):
        numero=numero//10
        cont=cont+1
    return (cont)

p=int(input('Digite p : '))
q=int(input('Digite q : '))
fim=0
while (q>0):
    x9= digitos(p)
    if (q%10**x9)==p:
        print('S')
        fim= fim +1
    else: 
        q=q//10
    
if fim==0:
    print('N')
else: 
    print('S')