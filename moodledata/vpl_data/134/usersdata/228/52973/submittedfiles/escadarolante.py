# -*- coding: utf-8 -*-
n=int(input('digite um valor:'))
lista=[]
for i in range(0,len(lista),1):
    tn=int(input('digite um tempo de passagem'))
    lista.append(tn)
    
def rolagem(a):
    for i in range (0,len(lista),1):
        tempo1=lista[i]+10
        if lista[i+1]>(lista[i]+10):
            tempo=tempo+(lista[i]-lista[i+1])
        elif lista[i+1]<=(lista[i]+10):
            tempo=tempo+10
    return(tempo)

print(rolagem(lista))
            





