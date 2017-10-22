# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO



def impar (x):
    if (x%2==0):
        return (False)
    else: 
        return (True)
        
n = 1000
while (n<=9999):
    if (impar (n) == True):
        ultimo = n%10
        penultimo = n%100
        antipenultimo = n%100
        primeiro = n//10
        soma = primeiro + antipenultimo - penultimo + ultimo
        if (soma <0):
            print (n)
    n = n+1
    
        
    
    