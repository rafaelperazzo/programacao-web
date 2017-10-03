# -*- coding: utf-8 -*-
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))
contador=0
if (a>=b):
    while(contador<1):
        cedula_a= c//a
        c=c%a
        cedula_b= c/b
        contador = contador+1
        if cedula_b == int(cedula_b):
            print(cedula_a)
            print(cedula_b)
        else:
            print('N')
else:
    while(contador<1):
        cedula_b= c//b
        c=c%b
        cedula_a= c/a
        contador = contador+1
        if cedula_a == int(cedula_a):
            print(cedula_b)
            print(cedula_a)
        else:
            print('N')
        
        
    