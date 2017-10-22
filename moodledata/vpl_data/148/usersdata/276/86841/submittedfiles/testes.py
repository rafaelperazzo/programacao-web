# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO



def impar (x):
    if (x%2==0):
        return (False)
    else: 
        return (True)
        
for n in range (1000,10000,1):
    n1 = n
    if (impar (n) == True):
        ultimo = n%10
        n = n//10
        penultimo = n%10
        n = n//10
        antipenultimo = n%10
        primeiro = n//10
        soma = primeiro - antipenultimo + penultimo - ultimo
        if (soma<0):
            print (n1)
    