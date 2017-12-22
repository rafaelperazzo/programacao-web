# -*- coding: utf-8 -*-

n = int(input('Digite a quantidade de elementos: '))
a = []
for i in range (0,n,1):
    valora = float(input('Digite o valor de a : '))
    a.append (valora)
for i in range (0,n,1):
    valorb = float(input('Digite o valor de b : '))
    b.append (valorb)
def lecker(x) :
    cont = 0
    for i in range (0,len(x),1) :
        if (i==0) :
            if x[i]>x[i+1] :
                cont = cont + 1
        elif (i==len(x)-1) :
            if x[i]>x[i-1] :
                cont = cont + 1
        else :
            if x[i]>x[i-1] and x[i]>x[i+1] :
                cont = cont + 1
        if (cont==1) :
            return(True)
        else :
            return(False)
if lecker(a) :
    print('S')
else :
    print('N')
if lecker(b) :
    print('S')
else :
    print('N')
