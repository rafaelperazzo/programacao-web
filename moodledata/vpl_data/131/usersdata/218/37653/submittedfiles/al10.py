# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite o valor de n:'))
numerador=2
denominador=1
i=1
termo=numerador/denominador
while i<=n+1:
    termo=termo*(numerador/denominador)
    if denominador<numerador:
        denominador=denominador+2
    else:
        numerador=numerador+2
    i=i+1    
    print('%.5f'%termo)