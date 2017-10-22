# -*- coding: utf-8 -*-
#ENTRADA
moedasA = int(input('Digite o valor das moedas A : '))
moedasB = int(input('Digite o valor das moedas B : '))
cedulaC = int(input('Digite o valor da cedula c : '))
z = 0
x9 = 0

#PROCESSAMENTO
while (z<cedulaC) :
    y = (moedasA*z)
    w = (z-y)
    if (w%cedulaC==0) :
        print(y)
        print(w)
        print('S')
        break
    else :
        z = z+1
        x9 = x9+1
if (x9==cedulaC) :
    print('N')
        
        

