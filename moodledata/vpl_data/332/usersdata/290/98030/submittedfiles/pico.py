# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    cont_c=0
    cont_d=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont_c+=1
        else:
            break
    for i in range(cont_c,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont_d+=1
        else:
            break
    if cont_c + cont_d== len(lista)-1 and cont_c>0 and cont_d>0:
        return ("S")
    else:
        return ("N")
lista=[]
n=int(input("Digite a quantidade de elementos: "))
#CONTINUE...
for i in range(0,n,1):
    lista.append(int(input("Digite o valor do %d elemeno: "%(i+1))))
print(pico(lista))