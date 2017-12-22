# -*- coding: utf-8 -*-
def media(lista):
    media= sum(lista)/len(lista)
    return media

def desvio(lista):
    somatorio=0
    for i in range(0,len(lista),1):
        somatorio= somatorio + ((lista[0]-media(lista))**2)
    desvio= ((somatorio/len(lista)**0.5))
    return desvio
    
print(desvio([1,2,3,4,5]))
print(desvio(10,20,30,40,50]))
