# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def feliz(n):
    p=0
    cont=0
    q=n
    while q!=0:
        q=q//10
        cont=cont+1
        for i in range(0,cont,1):
            soma=0
            while n>10:
                p=n%10
                n=n//10
                soma=soma+p**2
            n=soma
    if soma==1:
        return True
    else:
        return False
n=int(input('digite um numero oara ser testado se ele e ou nao feliz:')) 

if feliz(n):
    print ('Sim, ele é feliz')
else:
    print ('Não, ele não é feliz')