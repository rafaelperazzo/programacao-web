# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO



def impar (x):
    if (x%2==0):
        return (False)
    else: 
        return (True)
        
n = 1000
while (n<=9999):
    n1 = n
    if (impar (n1) == True):
        ultimo = n1%10
        n1 = n1//10
        penultimo = n1%10
        n1 = n1//10
        antipenultimo = n1%10
        primeiro = n1//10
        soma = primeiro - antipenultimo + penultimo - ultimo
        if (soma<0):
            print (n1)
    n = n+1
    
        
    
    