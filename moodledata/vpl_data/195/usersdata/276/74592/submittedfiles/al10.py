# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n = int(input('Digite o numero de termos: '))
numerador = 2
i = 1

while (numerador<=n):
    primeira = numerador/(numerador - i)
    segunda = numerador/(numerador + i) 
    pi2 = primeira*segunda
    i = i+1
    numerador = numerador + 2
    
print(pi2)
    

