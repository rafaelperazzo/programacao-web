# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n = int(input('Digite o numero de termos: '))
numerador = 2
contador = 1

while (contador<=n):
    primeira = numerador/(numerador - 1)
    segunda = numerador/(numerador + 1) 
    pi2 = primeira*segunda
    numerador = numerador + 2
    
pi = pi2*2
print(pi)
    

