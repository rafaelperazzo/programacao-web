# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n = int(input('Digite o numero de termos: '))
numerador = 2
denominador = 1
contador = 1
pi2 = 1

while (contador<=n):
    pi2 = pi2*(numerador/denominador)
    if ((numerador/denominador)<1):
        numerador = numerador + 2
    elif ((numerador/denominador)>1):
        denominador = denominador + 2 
        contador = contador + 1
    
pi = pi2*2
print('%.5f' %pi)
    

