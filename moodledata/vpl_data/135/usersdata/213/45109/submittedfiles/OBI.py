# -*- coding: utf-8 -*-
n=int(input('Informe o número de concorrentes: '))
p=int(input('Informe o número mínimo de pontos: '))

contador=0
for i in range(1,n+1,1):
    x=int(input('Informe o número de pontos obtidos na 1° Fase: '));
    y=int(input('Informe o número de pontos obtidos na 2° Fase: '));
    if (x+y)==p :
        contador=contador+1
        
print (contador)