# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def teste(numero):
    cont=0
    if numero==num:
        cont=cont+1
    if numero==num1:
        cont=cont+1
    if numero==num2:
        cont=cont+1
    if numero==num3:
        cont=cont+1
    if numero==num4:
        cont=cont+1
    if numero==num5:
        cont=cont+1
    return(cont)
    

a=int(input('digite o 1° número apostado: '))
b=int(input('digite o 2° número apostado: '))
c=int(input('digite o 3° número apostado: '))
d=int(input('digite o 4° número apostado: '))
e=int(input('digite o 5° número apostado: '))
f=int(input('digite o 6° número apostado: '))
num=int(input('digite o 1° número ganhador: '))
num1=int(input('digite o 2° número ganhador: '))
num2=int(input('digite o 3° número ganhador: '))
num3=int(input('digite o 4° número ganhador: '))
num4=int(input('digite o 5° número ganhador: '))
num5=int(input('digite o 6° número ganhador: '))

contg=0
contg=((teste(a))+(teste(b))+(teste(c))+(teste(d))+(teste(e))+(teste(f)))
if contg>0:
    if cont==3:
        print('Terno')
    elif cont==4:
        print('Quadra')
    elif cont==5:
        print('Quina')
    elif cont==6:
        print('Sena')
    else:
        print('azar')
else:
    print('azar')

    