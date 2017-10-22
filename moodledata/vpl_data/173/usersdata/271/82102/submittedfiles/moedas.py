# -*- coding: utf-8 -*-
#ENTRADA
moedasA = int(input('Digite o valor das moedas A : '))
moedasB = int(input('Digite o valor das moedas B : '))
cedulaC = int(input('Digite o valor da cedula c : '))
qa = 0
x9 = 0

#PROCESSAMENTO
while (z<cedulaC) :
    y = (moedasA*qa)
    w = cedulaC-(moedasA*qa)
    if (w%cedulaC==0) :
        print(z)
        print(w/moedasB)
        break
    else :
        z = z+1
        x9 = x9+1
if (x9==cedulaC) :
    print('N')
        
        

