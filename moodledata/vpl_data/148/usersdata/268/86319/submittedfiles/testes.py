# -*- coding: utf-8 -*-

a=int(input('Digite a : '))
q=int(input('Digite b : '))
cont=0
def digitos (n):
    cont=0
    while(n>0):
        cont=cont+1
        n=n//10
    return(cont)
    
while(q>0):
    conferir=q%10**digitos(q)
    if conferir==q:
        print('é Subnumero: ')
        cont=cont+1
        break
    else:
      q=q//10
if cont==0:
    print(' Não é subnumero ')
    


    