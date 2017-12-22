# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    cont1=0
    cont2=0
    cont3=0
    for i in range (1,len(a),1):
        if (a[i]>a[i-1]) and (cont2==0):
            cont1=cont1+1
        elif (a[i]<a[i-1]):
            cont2=cont2+1
        else:
            cont3=cont3+1
            break
    if (cont1+cont2==(len(a)-1)):
        return(True)
    else:
        return(False)

n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
for i in range (0,n,1):
    a.append(int(input('Digite o valor: ')))

    