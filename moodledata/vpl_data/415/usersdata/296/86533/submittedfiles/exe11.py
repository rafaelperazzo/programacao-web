# -*- coding: utf-8 -*-
n = int(input("Digite um número: "))
if n>99999999 or n<10000000:
    print ("NAO SEI")
else:
    soma = 0
    while (n > 0):
        resto = n%10
        n = (n - resto)/10
        soma = soma + resto
    print (soma)
    

      
 
        
   
    