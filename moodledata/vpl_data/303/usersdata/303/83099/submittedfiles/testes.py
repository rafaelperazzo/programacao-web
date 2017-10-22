# -*- coding: utf-8 -*-)
def conta_digitos(n):
    contador=1
    while(n//10>0):
        contador +=1
        n//10
    return contador 
print(conta_digitos(234567))


    

    
    