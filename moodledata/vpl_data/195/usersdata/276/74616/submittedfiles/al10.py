# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n = int(input('Digite o numero de termos: '))
numerador = 2
contador = 0
pi2 = 1

while (contador<=n):
    primeira = numerador/(numerador-1)
    segunda = numerador/(numerador+1)
    pi2 = pi2*primeira*segunda
    numerador = numerador + 2    
    contador = contador + 1
    
pi = pi2*2
print('%.5f' %pi)
    

