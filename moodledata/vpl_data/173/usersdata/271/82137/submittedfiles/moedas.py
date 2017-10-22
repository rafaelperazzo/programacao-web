# -*- coding: utf-8 -*-
#ENTRADA
moedasA = int(input('Digite o valor das moedas A : '))
moedasB = int(input('Digite o valor das moedas B : '))
cedulaC = int(input('Digite o valor da cedula c : '))
qa = 0
x9 = 0

#PROCESSAMENTO
while (qa<cedulaC) :
    y = (moedasA*qa)
    w = cedulaC-y
    if (w%moedasB==0) :
        print(qa)
        print(w/moedasB)
        break
    else :
        x9 = x9+1
        qa = qa+1
if (x9==cedulaC) :
    print('N')
        
        

