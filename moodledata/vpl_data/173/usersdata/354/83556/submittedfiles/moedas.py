# -*- coding: utf-8 -*-
moedasA=int(input('digite o valor das moedasA: '))
moedasB=int(input('digite o valor das moedasB: '))
cedulaC=int(input('digite o valor da cedulaC: '))
qa=0
x9=0

while (qa<cedulaC) :
    y = (moedasA*qa)
    w = cedulaC-y
    if (w%moedasB)==0 :
        print(qa)
        print(w/moedasB)
        break
    else:
         x9 = x9+1
         qa = qa+1
if (x9==cedulaC) :
    print('N')
