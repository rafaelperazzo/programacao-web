# -*- coding: utf-8 -*-

def pico(a):
    #CONTINUE...
    conta=0
    contb=0
    x9=0
    for i in range(1,len(a),1):
        if (a[i]>a[i-1]) and contb==0:
            conta=conta+1
        elif (a[i]<a[i-1]):
            contb=contb+1
        else:
             x9=x9+1
             break
    if conta + contb == len(a):
        return(True)
    else: 
        return(False)
    


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]

for i in range(0,n,1):
     valor=int(input('Digite o termo : '))
     a.append(valor)
     
if pico(a)==True:
    print('S')
if pico(a)==False:
    print('N')
